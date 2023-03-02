from rest_framework import serializers
from .models import BackgroundImagesForPages


class BackgroundImagesForPagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BackgroundImagesForPages
        fields = '__all__'


class SessionPathSerializer(serializers.Serializer):
    path = serializers.CharField()


class UnprocessedApplicationsSerializer(serializers.Serializer):
    unprocessed = serializers.IntegerField()
