from django.contrib import admin
from .models import *

# Register your models here.

class BoardGameAdmin(admin.ModelAdmin):
    pass

class BoardGameInstanceAdmin(admin.ModelAdmin):
    pass

class BoardGameRentalAdmin(admin.ModelAdmin):
    pass

class BoardGameReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(BoardGame, BoardGameAdmin)
admin.site.register(BoardGameInstance, BoardGameInstanceAdmin)
admin.site.register(BoardGameRental, BoardGameRentalAdmin)
admin.site.register(BoardGameReview, BoardGameReviewAdmin)