from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, GameListAPIView, GameDetailAPIView

router = DefaultRouter()
router.register(r'games', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('games/', GameListAPIView.as_view(), name='game-list'),
    path('games/<int:pk>/', GameDetailAPIView.as_view(), name='game-detail'),
]





