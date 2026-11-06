# etudiants/urls.py
from django.urls import path
from . import views

app_name = "etudiants"
urlpatterns = [
    path("", views.liste, name="liste"),
    path("recherche/", views.recherche, name="recherche"),
    path("<int:id>/", views.detail, name="detail"),
    path("api/", views.etudiants_api, name="api"),
    path("introuvable/", views.introuvable, name="introuvable"),
]
