from rest_framework.routers import DefaultRouter
from django.urls import path, include
from products.views import *


router=DefaultRouter()
router.register('category',CategoryViewSet)
router.register('product',ProductViewSet)
router.register('discount',DiscountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    # path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category-detail'),
]
