from django.urls import path
from .views import get_player, get_skills

urlpatterns = [
    path('player/', get_player),
    path('skills/', get_skills),
]