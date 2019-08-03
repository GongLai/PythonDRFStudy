from rest_framework import serializers

from goods.models import Brand
from fdfs_client.client import Fdfs_client
from django.conf import settings


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo', 'first_letter']

    def create(self, validated_data):
        # 1.fdfs文件上传
        # 1.1 获得上传的文件
        file = validated_data.pop('logo')
        content = file.read()

        # 1.2 获得fdfs连接对象
        client = Fdfs_client(settings.FDFS_CONFPATH)
        # 1.3 根据文件路径上传
        ret = client.upload_by_buffer(content)
        if ret['Status'] != 'Upload successed.':
            raise serializers.ValidationError('图片上传失败')

        # 2、获得文件上传后的file_id,在新建mysql数据(新建品牌对象)
        validated_data['logo'] = ret['Remote file_id']

        return super().create(validated_data)

    def update(self, instance, validated_data):
        file = validated_data.pop('logo')
        content = file.read()

        client = Fdfs_client(settings.FDFS_CONFPATH)
        ret = client.upload_by_buffer(content)
        if ret['Status'] != 'Upload successed.':
            raise serializers.ValidationError('图片上传失败')

        # 更新当前brand对象的logo字段
        logo = ret['Remote file_id']
        instance.logo = logo
        instance.save()

        return instance

