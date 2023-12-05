# filters.py
import django_filters as filters
from .models import Product , Discount , Category
from django.db.models import Sum

class CategoryFilter(filters.FilterSet):
 
    class Meta:
        model = Category
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }

class ProductFilter(filters.FilterSet):
    top_sales = filters.BooleanFilter(method='filter_top_sales')

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
        }
    def filter_top_sales(self, queryset, name, value):
        if value:
            return queryset.annotate(total_quantity_sold=Sum('orderitem__quantity')).order_by('-total_quantity_sold')
        return queryset


class DiscountFilter(filters.FilterSet):
    class Meta:
        model = Discount
        fields = "__all__"




