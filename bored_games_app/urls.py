from django.urls import path
from . import views

app_name = "bored_games"

urlpatterns = [
    # Home page / Landing page / Welcome page
    path("", views.landing_page, name = "landing"),

    # Page to display all available games
    path("games/", views.games_page, name = "games"),

    # Page for details of a single game
    path("games/<int:id>/", views.game_details, name = "game_detail"),

    # Form to add new game into database
    path("add_game/", views.new_games, name = "add_game"),

    # Form to add new review for a game
    path("add_review/<int:id>/", views.new_reviews, name = "add_review"),

    # Form to add new copy/instance of an existing game in the database (no template rendered)
    path("add_copy/<int:id>/", views.new_copy, name = "add_copy"),

    # Form to add copies of any existing game in the database (not only a particular game)
    path("add_copy/", views.new_copies, name = "add_copies"),

    # Form to rent an available copy/instance of a game (no template rendered)
    path("rent_game/<int:id>/", views.game_rentals, name = "rent_game"),

    # Page to view user's rented games and user's reviews
    path("profile/", views.user_rentals, name = "profile"),

    # Form to remove rental (no template rendered)
    path("remove_rental/<int:pk>/", views.rental_return, name = "remove_rental"),

    # Form to remove game instance added by user (no template rendered)
    path("remove_game_instance/<int:pk>/", views.game_instance_delete, name = "remove_game_instance"),

    # Form to edit user's existing review
    path("edit_review/<int:pk>/", views.review_edit, name = "edit_review"),

    # Form to delete review added by user (no template rendered)
    path("delete_review/<int:pk>/", views.delete_review, name = "delete_review"),

    # Form to register new user
    path("registration/", views.RegistrationView.as_view(), name = "registration")
]
