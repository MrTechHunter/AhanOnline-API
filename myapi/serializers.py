from rest_framework import serializers
from .models import Team
from .models import Systemusersview

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('teamid', 'name')

class SystemUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Systemusersview
        fields = ('firstname', 'gender')