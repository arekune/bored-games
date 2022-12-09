from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.

# VIEW FUNCTIONS

def landing_page(request):
    games = BoardGame.objects.count()
    game_instances = BoardGameInstance.objects.count()
    context = {
        "games": games,
        "game_instances": game_instances
    }
    return render(request, "bored_games_app/index.html", context = context)


def games_page(request):
    games = BoardGame.objects.filter(boardgameinstance__status="a").distinct()
    rented_games = BoardGame.objects.filter(boardgameinstance__status="r").distinct()

    if BoardGameRental.objects.filter(borrower = request.user.id).count() >= 3:
        limit_reached = True
    else:
        limit_reached = False
    
    if BoardGameInstance.objects.filter(status = "r").count() == 0:
        no_rentals = True
    else:
        no_rentals = False

    context = {
        "games": games,
        "rented_games": rented_games,
        "limit_reached": limit_reached,
        "no_rentals": no_rentals
        }

    return render(request, "bored_games_app/games.html", context = context)


def game_details(request, id):
    game = get_object_or_404(BoardGame, pk = id)
    reviews = BoardGameReview.objects.filter(game = id)
    context = {
        "game": game,
        "reviews": reviews
        }
    return render(request, "bored_games_app/game_detail.html", context = context)


@login_required
def new_games(request):

    if request.method == "POST":
        form = BoardGameForm(request.POST)

        if form.is_valid():
            game = form.save()
            BoardGameInstance.objects.get_or_create(game = game)
            return redirect(reverse("bored_games:game_detail", kwargs = {"id": game.id}))
        
    else:
        form = BoardGameForm()

    return render(request, "bored_games_app/add_game.html", context = {"form": form})


@login_required
def new_reviews(request):

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit = False)
            review.review_author = request.user
            review.save()
            return redirect(reverse("bored_games:game_detail", kwargs = {"id": review.game.id}))
    
    else:
        form = ReviewForm()

    return render(request, "bored_games_app/add_review.html", context = {"form": form})


@login_required
def new_copies(request):

    if request.method == "POST":
        form = BoardGameInstanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("bored_games:games"))
    
    else:
        form = BoardGameInstanceForm()
    
    return render(request, "bored_games_app/add_copy.html", context = {"form": form})


@login_required
def game_rentals(request):

    if request.method == "POST":
        form = BoardGameRentalForm(request.POST)

        if form.is_valid():
            game = form.save(commit = False)
            game.borrower = request.user
            game.save()
            obj, created = BoardGameInstance.objects.get_or_create(id = game.game_instance.id)
            obj.status = "r"
            obj.latest_borrower = request.user
            obj.save()
            return redirect(reverse("bored_games:profile"))
    
    else:
        form = BoardGameRentalForm()
    
    return render(request, "bored_games_app/rent_game.html", context = {"form": form})


@login_required
def user_rentals(request):
    rentals = BoardGameRental.objects.filter(borrower = request.user)
    reviews = BoardGameReview.objects.filter(review_author = request.user)

    context = {
        "rentals": rentals,
        "reviews": reviews
    }
    return render(request, "bored_games_app/my_rentals.html", context = context)


def rental_return(request, pk):
    rental = BoardGameRental.objects.get(pk = pk)
    obj, created = BoardGameInstance.objects.get_or_create(id = rental.game_instance.id)
    obj.status = "a"
    rental.delete()
    obj.save()
    return redirect(reverse("bored_games:profile"))


@login_required
def review_edit(request, pk):
    
    review = BoardGameReview.objects.get(pk = pk)

    if review.review_author != request.user:
        raise Http404
 
    if request.method != "POST":
        form = ReviewForm(instance = review)
    else:
        form = ReviewForm(instance = review, data = request.POST)
 
        if form.is_valid():
            form.save()
            return redirect("bored_games:profile")

    context = {
        "review": review,
        "form": form
        }

    return render(request, "bored_games_app/edit_review.html", context = context)


def delete_review(request, pk):
    review = BoardGameReview.objects.get(pk = pk)
    review.delete()
    return redirect(reverse("bored_games:profile"))
    

# CLASS-BASED VIEWS

class RegistrationView(CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "bored_games_app/registration.html"