from rest_framework import serializers
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for the login form.
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Incorrect username or password")
        return data
