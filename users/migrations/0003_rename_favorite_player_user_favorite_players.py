# Generated by Django 4.2.18 on 2025-03-31 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_favorite_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='favorite_player',
            new_name='favorite_players',
        ),
    ]
