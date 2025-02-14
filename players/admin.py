from django.contrib import admin
from .models import Player

# Register your models here.
class AdminPlayer(admin.ModelAdmin):
    list_display = ('name', 'id', )

admin.site.register(Player, AdminPlayer)
