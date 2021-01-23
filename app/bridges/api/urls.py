from django.urls import path
from bridges.api.views import (BridgeViewset, ManagementOrganizationViewset, InspectionViewset)

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash='/?')

router.register('bridges', BridgeViewset)
router.register('mngorganization', ManagementOrganizationViewset)
router.register('inspections', InspectionViewset)

urlpatterns = router.urls
