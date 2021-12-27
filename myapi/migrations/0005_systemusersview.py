# Generated by Django 2.1.15 on 2021-12-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Systemusersview',
            fields=[
                ('mainteamname', models.CharField(blank=True, db_column='MainTeamName', max_length=200, null=True)),
                ('systemuserid', models.CharField(db_column='SystemUserId', max_length=36)),
                ('organizationid', models.CharField(db_column='OrganizationId', max_length=36)),
                ('businessunitid', models.CharField(db_column='BusinessUnitId', max_length=36)),
                ('parentsystemuserid', models.CharField(blank=True, db_column='ParentSystemUserId', max_length=36, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=64, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=64, null=True)),
                ('fullname', models.CharField(blank=True, db_column='FullName', max_length=200, null=True)),
                ('internalemailaddress', models.CharField(blank=True, db_column='InternalEMailAddress', max_length=100, null=True)),
                ('mobilephone', models.CharField(blank=True, db_column='MobilePhone', max_length=64, null=True)),
                ('domainname', models.CharField(db_column='DomainName', max_length=1024)),
                ('createdon', models.DateTimeField(blank=True, db_column='CreatedOn', null=True)),
                ('modifiedon', models.DateTimeField(blank=True, db_column='ModifiedOn', null=True)),
                ('createdby', models.CharField(blank=True, db_column='CreatedBy', max_length=36, null=True)),
                ('modifiedby', models.CharField(blank=True, db_column='ModifiedBy', max_length=36, null=True)),
                ('isdisabled', models.BooleanField(blank=True, db_column='IsDisabled', null=True)),
                ('skills', models.CharField(blank=True, db_column='Skills', max_length=100, null=True)),
                ('calendarid', models.CharField(blank=True, db_column='CalendarId', max_length=36, null=True)),
                ('activedirectoryguid', models.CharField(blank=True, db_column='ActiveDirectoryGuid', max_length=36, null=True)),
                ('invitestatuscode', models.IntegerField(blank=True, db_column='InviteStatusCode', null=True)),
                ('isactivedirectoryuser', models.BooleanField(db_column='IsActiveDirectoryUser')),
                ('queueid', models.CharField(blank=True, db_column='QueueId', max_length=36, null=True)),
                ('transactioncurrencyid', models.CharField(blank=True, db_column='TransactionCurrencyId', max_length=36, null=True)),
                ('defaultmailbox', models.CharField(blank=True, db_column='DefaultMailbox', max_length=36, null=True)),
                ('userlicensetype', models.IntegerField(db_column='UserLicenseType')),
                ('islicensed', models.BooleanField(db_column='IsLicensed')),
                ('positionid', models.CharField(blank=True, db_column='PositionId', max_length=36, null=True)),
                ('positionidname', models.CharField(blank=True, db_column='PositionIdName', max_length=200, null=True)),
                ('test', models.IntegerField(blank=True, db_column='Test', null=True)),
                ('testdate', models.DateTimeField(blank=True, db_column='TestDate', null=True)),
                ('teststate', models.IntegerField(blank=True, db_column='TestState', null=True)),
                ('subsidiaryid', models.CharField(blank=True, db_column='SubsidiaryId', max_length=36, null=True)),
                ('notificationchatid', models.CharField(blank=True, db_column='NotificationChatId', max_length=100, null=True)),
                ('mainteam', models.CharField(blank=True, db_column='MainTeam', max_length=36, null=True)),
                ('currenttask', models.CharField(blank=True, db_column='CurrentTask', max_length=36, null=True)),
                ('ext', models.IntegerField(blank=True, db_column='EXT', null=True)),
                ('shamsidatestartcollaboration', models.CharField(blank=True, db_column='ShamsidateStartCollaboration', max_length=100, null=True)),
                ('id', models.IntegerField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('cats', models.TextField(blank=True, db_column='Cats', null=True)),
                ('onsite', models.IntegerField(blank=True, db_column='OnSite', null=True)),
                ('generateseller', models.TextField(blank=True, db_column='GenerateSeller', null=True)),
                ('happycustomerscount', models.IntegerField(blank=True, db_column='HappyCustomersCount', null=True)),
                ('unhappycustomerscount', models.IntegerField(blank=True, db_column='UnhappyCustomersCount', null=True)),
                ('mainproject', models.CharField(blank=True, db_column='MainProject', max_length=36, null=True)),
                ('parentmainteam', models.CharField(blank=True, db_column='ParentMainTeam', max_length=36, null=True)),
                ('defaultodbfoldername', models.CharField(db_column='DefaultOdbFolderName', max_length=200)),
                ('localimagelargeguid', models.CharField(blank=True, db_column='LocalImageLargeGuid', max_length=100, null=True)),
                ('localimagesmallguid', models.CharField(blank=True, db_column='LocalImageSmallGuid', max_length=100, null=True)),
                ('statusreason', models.IntegerField(blank=True, db_column='StatusReason', null=True)),
                ('birthday', models.CharField(blank=True, db_column='Birthday', max_length=36, null=True)),
                ('englishfamilyname', models.CharField(blank=True, db_column='EnglishFamilyName', max_length=30, null=True)),
                ('englishfirstname', models.CharField(blank=True, db_column='EnglishFirstName', max_length=30, null=True)),
                ('entrydate', models.CharField(blank=True, db_column='EntryDate', max_length=36, null=True)),
                ('gender', models.TextField(blank=True, db_column='Gender', null=True)),
                ('insurancestartdate', models.CharField(blank=True, db_column='InsuranceStartDate', max_length=36, null=True)),
                ('maritalstatus', models.TextField(blank=True, db_column='MaritalStatus', null=True)),
                ('nationalid', models.CharField(blank=True, db_column='NationalId', max_length=200, null=True)),
                ('numberofchildren', models.IntegerField(blank=True, db_column='NumberOfChildren', null=True)),
                ('realbirthday', models.CharField(blank=True, db_column='RealBirthday', max_length=36, null=True)),
                ('currentsalary', models.DecimalField(blank=True, db_column='CurrentSalary', decimal_places=0, max_digits=18, null=True)),
                ('systemuseridmeta', models.CharField(db_column='SystemUserIdMeta', max_length=36)),
            ],
            options={
                'db_table': 'SystemUsersView',
                'managed': False,
            },
        ),
    ]
