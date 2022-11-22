from django.contrib import admin
from .models import *

# Register your models here.

class BoardGameAdmin(admin.ModelAdmin):
    pass
admin.site.register(BoardGame, BoardGameAdmin)

class BoardGameInstanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(BoardGameInstance, BoardGameInstanceAdmin)

class BoardGameRentalAdmin(admin.ModelAdmin):
    pass
admin.site.register(BoardGameRental, BoardGameRentalAdmin)

class BoardGameReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(BoardGameReview, BoardGameReviewAdmin)