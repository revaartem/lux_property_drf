from rest_framework import serializers
from .models import BackgroundImagesForPages


class BackgroundImagesForPagesSerializer(serializers.ModelSerializer):
    """
    Serializer for BackgroundImagesForPages model.
    """
    class Meta:
        model = BackgroundImagesForPages
        fields = '__all__'


class SessionPathSerializer(serializers.Serializer):
    """
    Serializer for the session path.
    """
    path = serializers.CharField()


class UnprocessedApplicationsSerializer(serializers.Serializer):
    """
    Serializer for the number of unprocessed applications.
    """
    unprocessed = serializers.IntegerField()
