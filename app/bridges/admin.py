from django.contrib import admin
from .models import Bridge, ManagementOrganization, Inspection

admin.site.register(ManagementOrganization)
admin.site.register(Bridge)
admin.site.register(Inspection)
