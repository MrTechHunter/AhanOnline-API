from rest_framework import serializers
from .models import Team
from .models import Systemusersview

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('teamid', 'organizationid', 'businessunitid', 'name', 'description',
        'createdon', 'modifiedon', 'createdby', 'modifiedby', 'isdefault', 'administratorid',
        'queueid', 'teamtype', 'teamtemplateid', 'regardingobjecttypecode', 'manager',
        'salespurchasemanager', 'id', 'wegedetailaccount', 'poursantdetailaccount',
        'subsidiary', 'wegefactorsdetailaccount', 'poursantfactorsdetailaccount',
        'unitmanager', 'teampercentage', 'goal', 'usercount', 'newteamtype')

class SystemUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Systemusersview
        fields = ('mainteamname', 'systemuserid', 'organizationid', 'businessunitid', 'firstname', 'lastname', 'fullname', 'internalemailaddress')