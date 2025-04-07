import json
from players.models import Player
from django.core.management.base import BaseCommand
from datetime import datetime


class Command(BaseCommand):
    help = "Load data from JSON file"

    def handle(self, *args, **kwargs):
        with open("/home/terry-tech/fun-projects/django_players_backend/cleaned_player_data.json", "r") as fp:
            players_data = json.load(fp)
        # date_str = "Jan 15, 2023"
        def parse_date(date_str):
            if date_str:
                try:
                    return datetime.strptime(date_str, "%b %d, %Y")
                except ValueError:
                    return None
            return None

        for player in players_data:
            player_id = player.get('id')
            if player_id is None:
                self.stdout.write(self.style.WARNING(f"Skipping player with null ID: {player.get('name')}"))
                continue  
            # Remove the 'id' field from the player dictionary
            player.pop('id', None)

            # Parse date fields
            player['date_of_birth'] = parse_date(player.get("date_of_birth"))
            player['contract_expires'] = parse_date(player.get("contract_expires"))
            player['joined_date'] = parse_date(player.get("joined_date"))

            # Create or update the Player instance
            Player.objects.update_or_create(id=player_id, defaults=player)

        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
