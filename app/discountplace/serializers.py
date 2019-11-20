from rest_framework import serializers
from .models import *

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class FavoriteLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteLocation
        fields = '__all__'

class PlaceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceRequest
        fields = '__all__'