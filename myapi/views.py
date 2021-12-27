from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Team, TeamSerializer
from .serializers import Systemusersview, SystemUsersSerializer
from .models import Team
from .models import Systemusersview

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer

class SystemusersviewSet(viewsets.ModelViewSet):
    queryset = Systemusersview.objects.all().order_by('firstname')
    serializer_class = SystemUsersSerializer