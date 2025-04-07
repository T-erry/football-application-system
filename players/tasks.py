import json
from .models import Player
from celery import shared_task
from datetime import datetime
from django.conf import settings
import os
from django.db import transaction



#1. Task to count all player objects
@shared_task
def count_players():
    count_variable = Player.objects.count()

    return f"Total number of players: {count_variable}"

def parse_date(date_str):
    if date_str:
        try:
            #Jun 24, 1987
            return datetime.strptime(date_str, "%b %d, %Y")
        except:
            return None
    else:
        None
#2. Task to update Player database.
@shared_task
def update_players_from_json():
    json_file_path = os.path.join(settings.BASE_DIR, 'cleaned_player_data.json')
    
    try:
        with open(json_file_path, "r") as fp:
            players_data = json.load(fp)

        # Start a DB transaction
        with transaction.atomic():
            for player in players_data:
                  # Get player ID first
                player_id = player.get('id')
                if player_id is None:
                    print(f"Warning: Skipping player with null ID: {player.get('name')}")
                    continue
                
                # Remove the 'id' field from the player dictionary
                player.pop('id', None)
                
                # Parse date fields
                player['date_of_birth'] = parse_date(player.get("date_of_birth"))
                player['contract_expires'] = parse_date(player.get("contract_expires"))
                player['joined_date'] = parse_date(player.get("joined_date"))
                
                # Create or update the Player instance
                Player.objects.update_or_create(id=player_id, defaults=player)
               
            return f"Success: Player objects Updated."

    except Exception as e:
        # Log the error or return a failure message
        return f"Error updating player data: {str(e)}"