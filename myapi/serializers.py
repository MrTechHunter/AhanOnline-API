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
        fields = ('mainteamname', 'systemuserid', 'organizationid', 'businessunitid',
                  'parentsystemuserid', 'firstname', 'lastname', 'fullname', 'internalemailaddress',
                  'mobilephone', 'domainname', 'createdon', 'modifiedon', 'createdby', 'modifiedby',
                  'isdisabled', 'skills', 'calendarid', 'activedirectoryguid', 'invitestatuscode',
                  'isactivedirectoryuser', 'queueid', 'transactioncurrencyid', 'defaultmailbox',
                  'userlicensetype', 'islicensed', 'positionid', 'positionidname', 'test', 'testdate',
                  'teststate', 'subsidiaryid', 'notificationchatid', 'mainteam', 'currenttask',
                  'ext', 'shamsidatestartcollaboration', 'id', 'cats', 'onsite', 'generateseller',
                  'happycustomerscount', 'unhappycustomerscount', 'mainproject', 'parentmainteam',
                  'defaultodbfoldername', 'localimagelargeguid', 'localimagesmallguid', 'statusreason',
                  'birthday', 'englishfamilyname', 'englishfirstname', 'entrydate', 'gender',
                  'insurancestartdate', 'maritalstatus', 'nationalid', 'numberofchildren', 'realbirthday',
                  'currentsalary', 'systemuseridmeta')
