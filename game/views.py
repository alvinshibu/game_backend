from rest_framework import viewsets
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameListAPIView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetailAPIView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
