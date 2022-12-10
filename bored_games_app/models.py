from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class BoardGame(models.Model):
    """Model for each board game added into the database by users."""

    title = models.CharField(max_length = 100)
    min_no_of_players = models.IntegerField(validators = [MinValueValidator(1)])
    max_no_of_players = models.IntegerField(validators = [MinValueValidator(1)])
    summary = models.TextField(max_length = 200, null = True, blank = True)

    # Field is automatically set to date when object is first created
    date_added = models.DateField(auto_now_add = True)
    # Field is automatically set to now when object is saved
    date_modified = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse("bored_games:game_detail", kwargs = {"pk": self.pk})

    def __str__(self):
        return self.title

    
class BoardGameInstance(models.Model):
    """Model for each instance of a board game added into the database by users."""

    game = models.ForeignKey("BoardGame", on_delete = models.CASCADE)
    
    latest_borrower = models.ForeignKey(User, related_name = "latest_borrower", 
                                        on_delete = models.SET_NULL,
                                        null = True, blank = True)
                                        
    added_by = models.ForeignKey(User, related_name = "added_by",
                                on_delete = models.SET_NULL,
                                null = True, blank = True)

    LOAN_STATUS = (
        ("a", "Available"),
        ("r", "Rented")
    )

    status = models.CharField(max_length = 1, choices = LOAN_STATUS, default = "a")

    # Field is automatically set to date when object is first created
    date_added = models.DateField(auto_now_add = True)
    # Field is automatically set to now when object is saved
    date_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.id} {self.game.title}"


class BoardGameRental(models.Model):
    """Model for rentals of board game instances by users."""

    borrower = models.ForeignKey(User, on_delete = models.CASCADE)
    game_instance = models.ForeignKey("BoardGameInstance", on_delete = models.CASCADE)

    # Field is automatically set to date when object is first created
    date_rented = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.borrower} rented {self.game_instance.game.title} on {self.date_rented}"


class BoardGameReview(models.Model):
    """Model for reviews of board games written by users."""

    review = models.TextField()
    stars = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)], null = True, blank = True)
    
    game = models.ForeignKey("BoardGame", on_delete = models.RESTRICT, null = True)
    review_author = models.ForeignKey(User, on_delete = models.CASCADE)

    # Field is automatically set to date when object is first created
    date_written = models.DateField(auto_now_add = True)
    # Field is automatically set to now when object is saved
    date_edited = models.DateTimeField(auto_now = True)

    def __str__(self):
        """Return a string representation of the first 300 characters of a Review object's text."""
        return f"{self.review[:300]}"