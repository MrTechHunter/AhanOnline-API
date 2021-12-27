from django.contrib import admin
from .models import Team

# Register your models here.

# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('TeamId', 'OrganizationId', 'BusinessUnitId', 'Name', 'Description', 'CreatedOn', 'ModifiedOn', 'CreatedBy',
#     'ModifiedBy', 'IsDefault', 'AdministratorId', 'QueueId', 'TeamType', 'TeamTemplateId', 'RegardingObjectTypeCode', 'Manager',
#     'SalesPurchaseManager', 'Id', 'WegeDetailAccount', 'PoursantDetailAccount', 'Subsidiary', 'WegeFactorsDetailAccount',
#     'PoursantFactorsDetailAccount', 'UnitManager', 'TeamPercentage', 'Goal', 'UserCount', 'NewTeamType')
#     list_filter = ("CreatedBy",)
#     search_fields = ['Name', 'TeamId']

# admin.site.register(Team, TeamAdmin)