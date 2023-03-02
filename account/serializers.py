from rest_framework import serializers
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for the login form.

    Fields:
    - username (CharField): username field.
    - password (CharField): password field.

    Methods:
    - validate: validates the input data.

    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Validates the input data and authenticates the user.

        Args:
        - data (dict): input data.

        Returns:
        - data (dict): validated data.

        Raises:
        - serializers.ValidationError: if the username or password is incorrect.
        """
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Incorrect username or password")
        return data

