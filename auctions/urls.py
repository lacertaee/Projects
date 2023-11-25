from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("show/", views.show, name="show"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("add/", views.add, name="add"),
    path("remove/", views.remove, name="remove"),
    path("place_bid/", views.place_bid, name="place_bid"),
    path("close/", views.close, name='close'),
    path("page/", views.page, name='page'),
    path("category/", views.category, name='category'),
    path("comment/", views.comment, name='comment')
]
