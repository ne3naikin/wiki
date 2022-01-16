from django.urls import path

from . import views

#app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search/", views.search, name="search"),  # Пошук повинен щось виводити
    path("random_md/", views.random_md, name="random_md"),
    path("create_md/", views.create_md, name="create_md")
]
