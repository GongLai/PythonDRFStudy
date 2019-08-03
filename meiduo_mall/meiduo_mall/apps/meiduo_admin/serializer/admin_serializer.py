from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'mobile',
            'groups',
            'user_permissions',
            'password'
        ]

        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_staff'] = True

        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        return super().update(instance, validated_data)
