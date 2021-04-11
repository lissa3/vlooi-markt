from django.contrib import admin
from .models import MySite,CheckSite

admin.site.register(MySite)

class CheckSiteAdmin(admin.ModelAdmin):
    # search_fields = ('title', 'lead_text', 'main_text', 'categ', 'featured')
    list_display = ['id', 'time','site']

admin.site.register(CheckSite, CheckSiteAdmin)