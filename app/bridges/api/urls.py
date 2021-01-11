from django.urls import path
from bridges.api.views import (BridgeListCreateAPIView, BridgeDetailAPIView,
                               ManagementOrganizationCreateAPIView)


urlpatterns = [
    path("bridges/",
         BridgeListCreateAPIView.as_view(),
         name="bridge-list"),

    path("bridge/<int:pk>",
         BridgeDetailAPIView.as_view(),
         name="bridge-detail"),

    path("mngorganizations/",
         ManagementOrganizationCreateAPIView.as_view(),
         name="mngorganization-list"),


]
