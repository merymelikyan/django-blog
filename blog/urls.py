from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("add-post/", views.add_post, name="add_post"),
    path("contacts/", views.contacts, name="contacts"),
    path("login/", views.login, name="login"),
    path("article/<slug:article_slug>/", views.show_article, name="article"),
    path("category/<int:cat_id>/", views.show_category, name="category")
]