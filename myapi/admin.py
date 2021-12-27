from django.contrib import admin
from .models import Team
from .models import Systemusersview

# Register your models here.

### Team Model ###
class TeamAdmin(admin.ModelAdmin):
    list_filter = ("teamid", "createdby")
    search_fields = ['Name', 'TeamId']

admin.site.register(Team, TeamAdmin)


### Systemusersview Model ###
class SystemusersviewAdmin(admin.ModelAdmin):
    list_filter = ("mainteam", "createdby")
    search_fields = ['fullname', 'mobilephone']

admin.site.register(Systemusersview, SystemusersviewAdmin)