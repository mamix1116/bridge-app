from rest_framework import serializers
from bridges.models import ManagementOrganization, Bridge, Inspection, Damage

class BridgeSerializer(serializers.ModelSerializer):
    # management_organization = ManagementOrganizationSerializer(read_only=True)

    last_inspection = serializers.SerializerMethodField()

    class Meta:
        model = Bridge
        fields = ('id', 'bridge_id', 'bridge_name', 'bridge_name_yomi',
                  'location_city', 'location_address','road_cd', 'road_name', 'fyear_start',
                  'len_m', 'wid_m', 'span_num', 'latitude', 'longtitude', 'have_alternative',
                  'date_register', 'image_main', 'created_at', 'updated_at', 'management_organization',
                  'last_inspection')

    def get_last_inspection(self, obj):
        try:
            last_inspection = Inspection.objects.filter(bridge_name_id=obj.id).order_by('-date_inspect').first()
        except Exception as e:
            print(e)
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

class DamageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Damage
        fields = "__all__"

class InspectionSerializer(serializers.ModelSerializer):
    damages = DamageSerializer(many=True, read_only=True)

    class Meta:
        model = Inspection
        fields = "__all__"
