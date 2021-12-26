from django.db import models

# Create your models here.

class Team(models.Model):
    TeamId = models.CharField(primary_key=True, max_length=255, blank=True)
    OrganizationId = models.CharField(max_length=255, blank=True)
    BusinessUnitId = models.CharField(max_length=255, blank=True)
    Name = models.CharField(max_length=255, blank=True)
    Description = models.TextField(null=True, blank=True)
    CreatedOn = models.DateTimeField(null=True, blank=True)
    ModifiedOn = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    ModifiedBy = models.CharField(max_length=255, null=True, blank=True)
    IsDefault = models.BooleanField(max_length=255, blank=True)
    AdministratorId = models.CharField(max_length=255, blank=True)
    QueueId = models.CharField(max_length=255, null=True, blank=True)
    TeamType = models.IntegerField(blank=True)
    TeamTemplateId = models.CharField(max_length=255, null=True, blank=True)
    RegardingObjectTypeCode = models.IntegerField(null=True, blank=True)
    Manager = models.CharField(max_length=255, null=True, blank=True)
    SalesPurchaseManager = models.CharField(max_length=255, null=True, blank=True)
    Id = models.IntegerField(null=True)
    WegeDetailAccount = models.CharField(max_length=255, null=True, blank=True)
    PoursantDetailAccount = models.CharField(max_length=255, null=True, blank=True)
    Subsidiary = models.CharField(max_length=255, null=True, blank=True)
    WegeFactorsDetailAccount = models.CharField(max_length=255, null=True, blank=True)
    PoursantFactorsDetailAccount = models.CharField(max_length=255, null=True, blank=True)
    UnitManager = models.CharField(max_length=255, null=True, blank=True)
    TeamPercentage = models.DecimalField(max_digits=23, decimal_places=10, blank=True)
    Goal = models.CharField(max_length=255, null=True, blank=True)
    UserCount = models.IntegerField(null=True, blank=True)
    NewTeamType = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Name