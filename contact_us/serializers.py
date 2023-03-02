from rest_framework import serializers
from .models import ContactUs, ContactInfoLeft, Sources, MediaLinks


class ContactUsSerializer(serializers.ModelSerializer):
    """
    Serializer for the ContactUs model.

    Fields:
    - id: AutoField.
    - address: CharField.
    - phone: CharField.
    - email: EmailField.
    """
    class Meta:
        model = ContactUs
        fields = '__all__'


class ContactInfoLeftSerializer(serializers.ModelSerializer):
    """
    Serializer for the ContactInfoLeft model.

    Fields:
    - id: AutoField.
    - city: CharField.
    - address: CharField.
    """
    class Meta:
        model = ContactInfoLeft
        fields = '__all__'


class SourcesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Sources model.

    Fields:
    - id: AutoField.
    - title: CharField.
    """
    class Meta:
        model = Sources
        fields = '__all__'


class MediaLinksSerializer(serializers.ModelSerializer):
    """
    Serializer for the MediaLinks model.

    Fields:
    - id: AutoField.
    - title: CharField.
    - url: URLField.
    """
    class Meta:
        model = MediaLinks
        fields = '__all__'

