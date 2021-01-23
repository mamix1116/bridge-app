from rest_framework import serializers
from bridges.models import ManagementOrganization, Bridge, Inspection

class BridgeSerializer(serializers.ModelSerializer):
    # management_organization = ManagementOrganizationSerializer(read_only=True)

    last_inspection = serializers.SerializerMethodField()

    class Meta:
        model = Bridge
        fields = ('id', 'bridge_id', 'bridge_name', 'bridge_name_yomi',
                  'location_city', 'management_organization', 'last_inspection')

    def get_last_inspection(self, obj):
        try:
            last_inspection = models.Inspection.objects.filter(bridge_id=obj.id).order_by('-date_inspect').first()
        except Exception as e:
            return None
            if last_inspection is None:
                return None
            return InspectionSerializer(last_inspection).data


class ManagementOrganizationSerializer(serializers.ModelSerializer):
    bridges = BridgeSerializer(many=True, read_only=True)
    # bridges = serializers.HyperlinkedRelatedField(many=True,
    #                                            read_only=True,
    #                                            view_name="bridge-detail")

    class Meta:
        model = ManagementOrganization
        fields = "__all__"


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"
