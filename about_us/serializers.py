from rest_framework import serializers
from .models import AboutUsTopInfo, FirstBenefitsBlock, SecondBenefitsBlock, PhotosAndNumbers, TeamMember


class AboutUsTopInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsTopInfo
        fields = '__all__'


class FirstBenefitsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstBenefitsBlock
        fields = '__all__'


class SecondBenefitsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondBenefitsBlock
        fields = '__all__'


class PhotosAndNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotosAndNumbers
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'
