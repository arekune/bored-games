from django.urls import path
from . import views

app_name = "bored_games"

urlpatterns = [
    path("", views.landing_page_view, name = "landing"),
    path("games/<int:pk>/", views.GameDetail.as_view(), name = "game_detail")
]
