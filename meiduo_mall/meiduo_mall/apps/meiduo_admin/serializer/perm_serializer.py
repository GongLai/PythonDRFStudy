from rest_framework import serializers
from django.contrib.auth.models import Permission, ContentType, Group


class PermSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']



