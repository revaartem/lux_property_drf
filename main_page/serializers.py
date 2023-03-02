from rest_framework import serializers
from .models import HeroHeader, HeroBackgroundPhotos, Realtor, Property, PropertyPhoto, OurBenefits, CustomerSays


class HeroHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroHeader
        fields = '__all__'


class HeroBackgroundPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroBackgroundPhotos
        fields = '__all__'


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    realtor = RealtorSerializer()

    class Meta:
        model = Property
        fields = '__all__'


class PropertyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyPhoto
        fields = '__all__'


class OurBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurBenefits
        fields = '__all__'


class CustomerSaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSays
        fields = '__all__'
