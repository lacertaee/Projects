from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.get_title, name="titles"),
    path("search/", views.search, name="search"),
    path("create/", views.create_page, name="page"),
    path("change/", views.change_content, name="change"),
    path("chang/", views.change_c, name="change_c"),
    path("random/", views.random_entry, name="random")
]
