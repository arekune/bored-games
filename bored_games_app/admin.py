from django.contrib import admin
from .models import *

# Register your models here.

class BoardGameAdmin(admin.ModelAdmin):
    
    list_display = ("id", "title", "date_added", "date_modified")
    list_display_links = ("id", "title")
    ordering = ("id", "title")


class BoardGameInstanceAdmin(admin.ModelAdmin):
    
    list_display = ("id", "game", "status", "latest_borrower", "date_modified", "added_by", "date_added")
    list_display_links = ("id", "game")
    ordering = ("id", "game", "status", "latest_borrower", "date_modified", "added_by")

class BoardGameRentalAdmin(admin.ModelAdmin):

    list_display = ("id", "game_instance", "borrower", "date_rented")
    list_display_links = ("id", "game_instance")
    ordering = ("id", "game_instance", "borrower", "date_rented")

class BoardGameReviewAdmin(admin.ModelAdmin):
    
    list_display = ("id", "game", "review_author", "date_written", "date_edited")
    list_display_links = ("id", "game", "review_author")
    ordering = ("id", "game", "review_author", "date_written", "date_edited")

admin.site.register(BoardGame, BoardGameAdmin)
admin.site.register(BoardGameInstance, BoardGameInstanceAdmin)
admin.site.register(BoardGameRental, BoardGameRentalAdmin)
admin.site.register(BoardGameReview, BoardGameReviewAdmin)