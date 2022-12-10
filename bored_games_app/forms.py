from django.forms import ModelForm
from .models import *

class BoardGameForm(ModelForm):

    class Meta:
        model = BoardGame
        fields = "__all__"

        labels = {
            "title": "Title",
            "min_no_of_players": "Minimum number of players",
            "max_no_of_players": "Maximum number of players",
            "summary": "Summary"
        }

        error_messages = {
            "min_no_of_players": {
                "min_value": "Yo! Min value is 1!"
            },
            "max_no_of_players": {
                "min_value": "Yo! Min value is 1!"
            }
        }


class BoardGameInstanceForm(ModelForm):

    class Meta:
        model = BoardGameInstance
        fields = ["game"]


class BoardGameRentalForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BoardGameRentalForm, self).__init__(*args, **kwargs)
        self.fields["game_instance"].queryset = BoardGameInstance.objects.filter(status="a")

    class Meta:
        model = BoardGameRental
        fields = ["game_instance"]

        labels = {
            "game_instance": "Choose a game"
        }


class ReviewForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["game"].widget.attrs["readonly"] = True

    class Meta:
        model = BoardGameReview
        fields = ["game", "review"]

        labels = {
            "game": "Game",
            "review": "Review"
        }