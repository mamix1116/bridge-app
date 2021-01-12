from rest_framework import serializers
from bridges.models import ManagementOrganization, Bridge

class BridgeSerializer(serializers.ModelSerializer):
    # management_organization = ManagementOrganizationSerializer(read_only=True)

    class Meta:
        model = Bridge
        fields = "__all__"


class ManagementOrganizationSerializer(serializers.ModelSerializer):
    bridges = BridgeSerializer(many=True, read_only=True)
    # bridges = serializers.HyperlinkedRelatedField(many=True,
    #                                            read_only=True,
    #                                            view_name="bridge-detail")

    class Meta:
        model = ManagementOrganization
        fields = "__all__"
