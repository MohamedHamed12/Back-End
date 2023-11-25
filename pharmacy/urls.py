from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(r'pharmacy', PharmacyViewSet, basename='pharmacy')
router.register('productitem',ProductItemViewSet)
router.register('prescription',PrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
   
]
