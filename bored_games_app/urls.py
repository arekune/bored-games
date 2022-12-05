from django.urls import path
from . import views

app_name = "bored_games"

urlpatterns = [
    path("", views.landing_page_view, name = "landing"),
    path("games/", views.games_page_view, name="games")
]
