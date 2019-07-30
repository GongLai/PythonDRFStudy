from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'mobile',
            'email',
            'password'
        ]

        extra_kwargs = {
            'password': {
                "write_only": True
            }
        }

    # 重写create方法
    def create(self, validated_data):


        return self.Meta.model.objects.create_superuser(**validated_data)
