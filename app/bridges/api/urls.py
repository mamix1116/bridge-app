from django.urls import path
from bridges.api.views import (BridgeViewset, ManagementOrganizationViewset, InspectionViewset, DamageViewset)

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash='/?')

router.register('bridges', BridgeViewset)
router.register('mngorganization', ManagementOrganizationViewset)
router.register('inspections', InspectionViewset)
router.register('damages', DamageViewset)

urlpatterns = router.urls
