from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("newPage/", views.newPage, name="newPage"),
    path("editPage/", views.editPage, name="editPage"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("<str:title>/", views.entry, name="entry"),
]
