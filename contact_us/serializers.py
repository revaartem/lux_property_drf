from rest_framework import serializers
from .models import ContactUs, ContactInfoLeft, Sources, MediaLinks


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class ContactInfoLeftSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfoLeft
        fields = '__all__'


class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = '__all__'


class MediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLinks
        fields = '__all__'

