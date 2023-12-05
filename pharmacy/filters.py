# filters.py
import django_filters as filters
from .models import *
class PharmacyFilter(filters.FilterSet):
    class Meta:
        model =  Pharmacy
        fields = "__all__"

