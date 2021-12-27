from django.db import models

# Create your models here.

# class Team(models.Model):
#     TeamId = models.CharField(primary_key=True, max_length=255, blank=True)
#     OrganizationId = models.CharField(max_length=255, blank=True)
#     BusinessUnitId = models.CharField(max_length=255, blank=True)
#     Name = models.CharField(max_length=255, blank=True)
#     Description = models.TextField(null=True, blank=True)
#     CreatedOn = models.TextField(max_length=255, null=True, blank=True)
#     ModifiedOn = models.TextField(max_length=255, null=True, blank=True)
#     CreatedBy = models.CharField(max_length=255, null=True, blank=True)
#     ModifiedBy = models.CharField(max_length=255, null=True, blank=True)
#     IsDefault = models.BooleanField(max_length=255, blank=True)
#     AdministratorId = models.CharField(max_length=255, blank=True)
#     QueueId = models.CharField(max_length=255, null=True, blank=True)
#     TeamType = models.IntegerField(blank=True)
#     TeamTemplateId = models.CharField(max_length=255, null=True, blank=True)
#     RegardingObjectTypeCode = models.IntegerField(null=True, blank=True)
#     Manager = models.CharField(max_length=255, null=True, blank=True)
#     SalesPurchaseManager = models.CharField(max_length=255, null=True, blank=True)
#     Id = models.IntegerField(null=True)
#     WegeDetailAccount = models.CharField(max_length=255, null=True, blank=True)
#     PoursantDetailAccount = models.CharField(max_length=255, null=True, blank=True)
#     Subsidiary = models.CharField(max_length=255, null=True, blank=True)
#     WegeFactorsDetailAccount = models.CharField(max_length=255, null=True, blank=True)
#     PoursantFactorsDetailAccount = models.CharField(max_length=255, null=True, blank=True)
#     UnitManager = models.CharField(max_length=255, null=True, blank=True)
#     TeamPercentage = models.DecimalField(max_digits=23, decimal_places=10, blank=True)
#     Goal = models.CharField(max_length=255, null=True, blank=True)
#     UserCount = models.IntegerField(null=True, blank=True)
#     NewTeamType = models.IntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.Name

class Team(models.Model):
    teamid = models.CharField(db_column='TeamId', max_length=36)  # Field name made lowercase.
    organizationid = models.CharField(db_column='OrganizationId', max_length=36)  # Field name made lowercase.
    businessunitid = models.CharField(db_column='BusinessUnitId', max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=160)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='ModifiedOn', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.
    administratorid = models.CharField(db_column='AdministratorId', max_length=36)  # Field name made lowercase.
    queueid = models.CharField(db_column='QueueId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    teamtype = models.IntegerField(db_column='TeamType')  # Field name made lowercase.
    teamtemplateid = models.CharField(db_column='TeamTemplateId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    regardingobjecttypecode = models.IntegerField(db_column='RegardingObjectTypeCode', blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=36, blank=True, null=True)  # Field name made lowercase.
    salespurchasemanager = models.CharField(db_column='SalesPurchaseManager', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    wegedetailaccount = models.CharField(db_column='WegeDetailAccount', max_length=36, blank=True, null=True)  # Field name made lowercase.
    poursantdetailaccount = models.CharField(db_column='PoursantDetailAccount', max_length=36, blank=True, null=True)  # Field name made lowercase.
    subsidiary = models.CharField(db_column='Subsidiary', max_length=36, blank=True, null=True)  # Field name made lowercase.
    wegefactorsdetailaccount = models.CharField(db_column='WegeFactorsDetailAccount', max_length=36, blank=True, null=True)  # Field name made lowercase.
    poursantfactorsdetailaccount = models.CharField(db_column='PoursantFactorsDetailAccount', max_length=36, blank=True, null=True)  # Field name made lowercase.
    unitmanager = models.CharField(db_column='UnitManager', max_length=36, blank=True, null=True)  # Field name made lowercase.
    teampercentage = models.DecimalField(db_column='TeamPercentage', max_digits=23, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    goal = models.CharField(db_column='Goal', max_length=36, blank=True, null=True)  # Field name made lowercase.
    usercount = models.IntegerField(db_column='UserCount', blank=True, null=True)  # Field name made lowercase.
    newteamtype = models.IntegerField(db_column='NewTeamType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Team'