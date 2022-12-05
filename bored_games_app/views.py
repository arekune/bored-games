from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from . models import BoardGame, BoardGameInstance, BoardGameRental, BoardGameReview


# Create your views here.

# VIEW FUNCTIONS

def landing_page_view(request):
    return render(request, "bored_games_app/index.html")

def games_page_view(request):
    boardgames = BoardGameRental.objects.filter(borrower= request.user).order_by("date_rented")
    context = {"boardgames" : boardgames}
    return render(request, "bored_games_app/games.html", context)
