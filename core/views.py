from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player, Skill
from .serializers import PlayerSerializer, SkillSerializer


@api_view(['GET'])
def get_player(request):
    player = Player.objects.first()
    serializer = PlayerSerializer(player)
    return Response(serializer.data)


@api_view(['GET'])
def get_skills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)