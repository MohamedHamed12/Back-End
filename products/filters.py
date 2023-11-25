# filters.py
import django_filters as filters
from .models import Product , Discount , Category

class CategoryFilter(filters.FilterSet):
 
    class Meta:
        model = Category
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }

class ProductFilter(filters.FilterSet):
   

    class Meta:
        model = Product
        fields={
            'name': ['exact', 'icontains', 'istartswith'],
            'generic_name': ['exact', 'icontains', 'istartswith'],
            'form': ['exact', 'icontains', 'istartswith'],
            'strength': ['exact', 'icontains', 'istartswith'],
            'factory_company': ['exact', 'icontains', 'istartswith'],
            'category__name': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'price': ['gte', 'lte', 'gt', 'lt'],
            'sales': ['gte', 'lte', 'gt', 'lt'],
        }

class DiscountFilter(filters.FilterSet):
    class Meta:
        model = Discount
        fields = "__all__"




