from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('TeamId', 'OrganizationId', 'OrganizationId', 'BusinessUnitId', 'Name',
                 'Description', 'CreatedOn', 'ModifiedOn', 'CreatedBy', 'ModifiedBy',
                 'IsDefault', 'AdministratorId', 'QueueId', 'TeamType', 'TeamTemplateId',
                 'RegardingObjectTypeCode', 'Manager', 'SalesPurchaseManager', 'Id',
                 'WegeDetailAccount', 'PoursantDetailAccount', 'Subsidiary', 'WegeFactorsDetailAccount',
                 'PoursantFactorsDetailAccount', 'UnitManager', 'TeamPercentage', 'Goal', 'UserCount',
                 'NewTeamType',
                 )