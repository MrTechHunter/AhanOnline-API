from django.contrib import admin
from .models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_filter = ("teamid", "createdby")
    search_fields = ['Name', 'TeamId']

admin.site.register(Team, TeamAdmin)