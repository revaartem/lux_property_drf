"""
Module serializers.py

This module contains serializers for the About Us app models.
"""

from rest_framework import serializers
from .models import AboutUsTopInfo, FirstBenefitsBlock, SecondBenefitsBlock, PhotosAndNumbers, TeamMember


class AboutUsTopInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for AboutUsTopInfo model.
    """
    class Meta:
        model = AboutUsTopInfo
        fields = '__all__'


class FirstBenefitsBlockSerializer(serializers.ModelSerializer):
    """
    Serializer for FirstBenefitsBlock model.
    """
    class Meta:
        model = FirstBenefitsBlock
        fields = '__all__'


class SecondBenefitsBlockSerializer(serializers.ModelSerializer):
    """
    Serializer for SecondBenefitsBlock model.
    """
    class Meta:
        model = SecondBenefitsBlock
        fields = '__all__'


class PhotosAndNumbersSerializer(serializers.ModelSerializer):
    """
    Serializer for PhotosAndNumbers model.
    """
    class Meta:
        model = PhotosAndNumbers
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    """
    Serializer for TeamMember model.
    """
    class Meta:
        model = TeamMember
        fields = '__all__'
