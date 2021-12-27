# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
