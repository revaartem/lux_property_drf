from rest_framework import serializers
from .models import HeroHeader, HeroBackgroundPhotos, Realtor, Property, PropertyPhoto, OurBenefits, CustomerSays


class HeroHeaderSerializer(serializers.ModelSerializer):
    """
    Serializer for HeroHeader model.
    """
    class Meta:
        model = HeroHeader
        fields = '__all__'


class HeroBackgroundPhotosSerializer(serializers.ModelSerializer):
    """
    Serializer for HeroBackgroundPhotos model.
    """
    class Meta:
        model = HeroBackgroundPhotos
        fields = '__all__'


class RealtorSerializer(serializers.ModelSerializer):
    """
    Serializer for Realtor model.
    """
    class Meta:
        model = Realtor
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer for Property model.
    """
    realtor = RealtorSerializer()

    class Meta:
        model = Property
        fields = '__all__'


class PropertyPhotoSerializer(serializers.ModelSerializer):
    """
    Serializer for PropertyPhoto model.
    """
    class Meta:
        model = PropertyPhoto
        fields = '__all__'


class OurBenefitsSerializer(serializers.ModelSerializer):
    """
    Serializer for OurBenefits model.
    """
    class Meta:
        model = OurBenefits
        fields = '__all__'


class CustomerSaysSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomerSays model.
    """
    class Meta:
        model = CustomerSays
        fields = '__all__'
