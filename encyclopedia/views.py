from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

markdowner = Markdown()

def substring(title):
    sub_entry = set()
    for i in title:
        if i.lower() in "python":
            sub_entry.add("Python")
        if i.lower() in "git":
            sub_entry.add("Git")
        if i.lower() in "css":
            sub_entry.add("CSS")
        if i.lower() in "django":
            sub_entry.add("Django")
        if i.lower() in "html":
            sub_entry.add("HTML")
    return sub_entry
    

def html_to_md(title):
    file = util.get_entry(title)
    if file == None:
        return None
    else:
        return markdowner.convert(file)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_title(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    else:
        title1 = html_to_md(title)
        return render(request, "encyclopedia/show.html", {
            "ent": title1,
            "title": title
        })
    
def search(request):
    if request.method == "POST":
        f = request.POST["q"]
        html = html_to_md(f)
        if html is not None:
            return render(request, "encyclopedia/show.html", {
                "ent": html
            })
        else:
            return render(request, "encyclopedia/search.html", {
                "sub": substring(f)
            })

def create_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    else:
        f = request.POST["title"]
        entries = util.get_entry(f)
        mark = request.POST["cont"]
        if entries is not None:
            return render(request, "encyclopedia/error1.html")
        else:
            util.save_entry(f, mark)
            return render(request, "encyclopedia/show.html", {
                "ent": markdowner.convert(mark)
            })

def change_content(request):
    if request.method == "POST":
        title = request.POST["entry_name"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/change.html", {
            "content": content
        })
    else:
        return None
    
def change_c(request):
    if request.method == "POST":
        content = request.POST["new_content"]
        return render(request, "encyclopedia/show.html", {
            "ent": markdowner.convert(content)
        })
    
def random_entry(request):
    choices = util.list_entries()
    picked = random.choice(choices)
    finished = util.get_entry(picked)
    return render(request, "encyclopedia/show.html", {
        "ent": markdowner.convert(finished)
    })
    
        



    
      
