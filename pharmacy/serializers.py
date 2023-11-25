from rest_framework import serializers
from .models import  *

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'
class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Prescription
        fields = '__all__'

