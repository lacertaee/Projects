from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Watchlist, Category, Bids, Comments


def index(request):
    return render(request, "auctions/index.html",{
        "listings": Listing.objects.all(),
        "category": Category.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "GET":
        return render(request, "auctions/create.html", {
            'category': Category.objects.all()
        })
    else:
        description1 = request.POST["description"]
        url1 = request.POST["url"]
        bid1 = float(request.POST["bid"])
        bid = format(bid1, '.2f')
        title1 = request.POST["title"]
        user = request.user
        category = Category.objects.get(categoryN=request.POST['category'])
        Listing(category=category, owner=user, description=description1, url=url1, starting_bid=bid, title=title1).save()
        Bids(title=title1, bids=bid, owner=request.user).save()
        return HttpResponseRedirect(reverse("index"))

def show(request):
    f = request.POST['id']
    h = request.POST['title1']
    return render(request, "auctions/show.html", {
        "listing": Listing.objects.get(pk=f),
        'user': request.user,
        'comments': Comments.objects.filter(title=h)
    })

@login_required
def watchlist(request):
    fav = Watchlist.objects.all()
    return render(request, "auctions/watchlist.html", {
        "watchlists": fav,
        'user': request.user
    })

@login_required
def add(request):
    f = request.POST['id']
    h = Listing.objects.get(pk=f)
    title = h.title
    url = h.url
    description = h.description
    bid = float(h.starting_bid)
    Watchlist(bid=format(bid, '.2f'), title=title, url=url, description=description, owner=request.user).save()
    return HttpResponseRedirect(reverse("watchlist"))

def remove(request):
    f = request.POST['remove']
    Watchlist.objects.get(pk=f).delete()
    return HttpResponseRedirect(reverse("watchlist"))

@login_required
def place_bid(request):
    price = float(request.POST['price'])
    listing = Listing.objects.get(pk=int(request.POST['id']))
    bid = float(request.POST['bid'])
    all_bids = Bids.objects.get(title=listing.title)
    if bid >= price:
        listing.starting_bid = bid
        listing.save()
        all_bids.bids = bid
        owner = request.user
        all_bids.owner = owner
        all_bids.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/show.html", {
            "listing": Listing.objects.get(pk=int(request.POST['id'])),
            "error": "Provided bid is less than the current bid!",
            "comments": Comments.objects.filter(title=listing.title)
        })
    
def close(request):
    title = request.POST['title']
    winner = Bids.objects.get(title=title)
    listing = Listing.objects.get(title=title)
    listing.delete()
    return render(request, "auctions/winner.html", {
        'winner': winner.owner
    })

def page(request):
    title = request.POST["title"]
    f = Listing.objects.get(title=title)
    return render(request, "auctions/show.html", {
        "listing": f,
        'user': request.user,
        'comments': Comments.objects.all()
    })

def category(request):
    category1 = request.POST['category']
    f = Category.objects.get(categoryN=category1)
    h = Listing.objects.filter(category=f)
    return render(request, 'auctions/index.html', {
        "listings": h,
        "category": Category.objects.all()
    })

@login_required
def comment(request):
    comment1 = request.POST['com']
    Comments(title=request.POST['title'], comment=comment1, owner=request.user).save()
    return render(request, "auctions/show.html", {
        "listing": Listing.objects.get(pk=request.POST['id']),
        'user': request.user,
        'comments': Comments.objects.filter(title=request.POST['title'])
    })
    

