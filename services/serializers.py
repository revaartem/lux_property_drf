from rest_framework import serializers
from .models import ServicesInfoOffer


class ServicesInfoOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesInfoOffer
        fields = '__all__'

