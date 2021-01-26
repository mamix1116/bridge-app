from django.contrib import admin
from .models import Bridge, ManagementOrganization, Inspection, Damage

class BridgeAdmin(admin.ModelAdmin):
    list_display = ('bridge_id', 'bridge_name', 'bridge_name_yomi', 'road_name', 'management_organization')
    list_display_links = ('bridge_id', 'bridge_name')
    list_filter = ('management_organization',)
    search_fields = ('bridge_name', 'bridge_name_yomi', 'road_name')
    list_per_page = 50

class InspectionAdmin(admin.ModelAdmin):
    list_display = ('bridge_name', 'date_inspect', 'eval_overall')
    list_display_links = ('bridge_name', 'date_inspect')
    list_filter = ('bridge_name',)


admin.site.register(ManagementOrganization)
admin.site.register(Bridge, BridgeAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Damage)
