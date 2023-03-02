from rest_framework import serializers
from .models import ServicesInfoOffer


class ServicesInfoOfferSerializer(serializers.ModelSerializer):
    """
    Serializer for ServicesInfoOffer model.
    """

    class Meta:
        model = ServicesInfoOffer
        fields = '__all__'

