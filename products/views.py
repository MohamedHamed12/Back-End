from rest_framework import viewsets

from products.filters import ProductFilter, DiscountFilter , CategoryFilter
from .models import *
from .serializers import *
# from django_filters import rest_framework as filters
# from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class  = CategoryFilter
    # filterset_fields = {
    #     "name": ["icontains", "startswith", "exact"],
        
    # }


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    def get_top_selling_products(self):
        top_products = Product.objects.annotate(total_sales=Sum('orderitem__quantity')).order_by('-total_sales')
        serializer = ProductSerializer(top_products, many=True)
        return Response(serializer.data)
class  DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    filterset_class = DiscountFilter


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer