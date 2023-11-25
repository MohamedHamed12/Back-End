from .models import *
from rest_framework import viewsets
from .serializers import *
class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset =  Prescription.objects.all()
    serializer_class =  PrescriptionSerializer

    