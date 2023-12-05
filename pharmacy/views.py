from .models import *
from rest_framework import viewsets
from .serializers import *
class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


    