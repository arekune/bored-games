from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from . import models

# Create your views here.

# VIEW FUNCTIONS

def landing_page_view(request):
    return render(request, "bored_games_app/index.html")

# CLASS-BASED VIEWS

class GameDetail(DetailView):

    model = models.BoardGame