from rest_framework import serializers

from goods.models import SKUImage, SKU
from fdfs_client.client import Fdfs_client
from django.conf import settings


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKUImage
        fields = ['id', 'sku', 'image']

    def create(self, validated_data):
        file = validated_data.pop('image')
        content = file.read()

        client = Fdfs_client(settings.FDFS_CONFPATH)
        ret = client.upload_by_buffer(content)
        if ret['Status'] != 'Upload successed.':
            raise serializers.ValidationError('图片上传失败')

        validated_data['image'] = ret['Remote file_id']

        return super().create(validated_data)

    def update(self, instance, validated_data):
        file = validated_data.pop('image')
        content = file.read()

        client = Fdfs_client(settings.FDFS_CONFPATH)
        ret = client.upload_by_buffer(content)
        if ret['Status'] != 'Upload successed.':
            raise serializers.ValidationError('图片上传失败')

        image = ret['Remote file_id']
        instance.image = image
        instance.save()

        return instance


class SimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ['id', 'name']