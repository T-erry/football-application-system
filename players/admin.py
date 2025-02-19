from django.contrib import admin
from .models import Player
from django.db.models import F

# Register your models here.admin.site.register(Player, AdminPlayer)
@admin.register(Player)
class AdminPlayer(admin.ModelAdmin):
    def formatted_market_value(self, obj):
        return f"{obj.market_value:,}" if obj.market_value is not None else "N/A"
    
    formatted_market_value.short_description ="Market_Value" 

    list_display = ["id", "name", "age", "caps", "formatted_market_value", "league_name", "league_level"]
    search_fields = ['id', "name"]
    #adding filters
    list_filter = ['league_name']
    ordering = [
            F("market_value").desc(nulls_last=True),
            F("caps").desc(nulls_last=True),
        ]
    fieldsets = (
        (
            'Personal Info',{
                'fields':("name", "date_of_birth", "place_of_birth", "citizenship", "age", "place_of_birth_flag")
            }
        ),
             
        (
            'Professional Info',{
                'fields':("club", "national_team", "caps", "international_goals", "market_value", "main_position")
            }
        ),
        (
            'Additional Info',{
                'fields':("agency_info", "club_stats", "national_team_stats", "current_season_stats")
            }
        )
    )

