from django.contrib import admin
from .models import Bridge, ManagementOrganization

admin.site.register(ManagementOrganization)
admin.site.register(Bridge)
