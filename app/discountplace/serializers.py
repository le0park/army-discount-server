from rest_framework import serializers
from .models import *

class CustomSerializer(serializers.ModelSerializer):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class PlaceSerializer(CustomSerializer):
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.like_set.count()

    class Meta:
        model = Place
        fields = '__all__'
        extra_fields = ['likes']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
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