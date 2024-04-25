from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'minimumvalue', 'maximumvalue']  # Include 'id' for referencing in API URLs
