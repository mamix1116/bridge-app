from rest_framework import generics
from rest_framework import mixins
# from rest_framework import status
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView

from rest_framework import viewsets


from bridges.models import Bridge, ManagementOrganization, Inspection, Damage
from bridges.api.serializers import BridgeSerializer, ManagementOrganizationSerializer, InspectionSerializer, DamageSerializer

class BridgeViewset(viewsets.ModelViewSet):
    queryset = Bridge.objects.all()
    serializer_class = BridgeSerializer


class ManagementOrganizationViewset(viewsets.ModelViewSet):
    queryset = ManagementOrganization.objects.all()
    serializer_class = ManagementOrganizationSerializer


class InspectionViewset(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

class DamageViewset(viewsets.ModelViewSet):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer


class BridgeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bridge.objects.all()
    serializer_class = BridgeSerializer

class BridgeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bridge.objects.all()
    serializer_class = BridgeSerializer

class ManagementOrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = ManagementOrganization.objects.all()
    serializer_class = ManagementOrganizationSerializer

# class BridgeListCreateAPIView(APIView):
#
#     def get(self, request):
#         bridges = Bridge.objects.all()
#         serializer = BridgeSerializer(bridges, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BridgeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class BridgeDetailAPIView(APIView):
#
#     def get_object(self, pk):
#         bridge = get_object_or_404(Bridge, pk=pk)
#         return bridge
#
#     def get(self, request, pk):
#         bridge = self.get_object(pk)
#         serializer = BridgeSerializer(bridge)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         bridge = self.get_object(pk)
#         serializer = BridgeSerializer(bridge, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         bridge = self.get_object(pk)
#         bridge.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# class ManagementOrganizationListCreateAPIView(APIView):
#
#     def get(self, request):
#         management_organizations = ManagementOrganization.objects.all()
#         serializer = ManagementOrganizationSerializer(management_organizations,
#                                                       many=True,
#                                                       context={'request':request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ManagementOrganizationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
