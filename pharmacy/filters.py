# filters.py
import django_filters as filters
from .models import *
class PharmacyFilter(filters.FilterSet):
    class Meta:
        model =  Pharmacy
        fields = "__all__"
class ProductItemFilter(filters.FilterSet):
    class Meta:
        model =  ProductItem
        fields = "__all__"
class PrescriptionFilter(filters.FilterSet):
    class Meta:
        model =  Prescription
        fields = "__all__"
