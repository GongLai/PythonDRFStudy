from rest_framework import serializers

from goods.models import *


class SKUSpecsSerializer(serializers.ModelSerializer):

    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ['option_id', 'spec_id']


class SKUSerializer(serializers.ModelSerializer):

    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    category = serializers.StringRelatedField()

    specs = SKUSpecsSerializer(many=True)

    class Meta:
        model = SKU
        fields = "__all__"

    def create(self, validated_data):
        """新建单一sku对象的时候，手动构建中间表数据，来保存规格和选项信息"""

        specs = validated_data.pop("specs")
        # 创建从表数据对象之前，先构建主表sku对象
        instance = super().create(validated_data)
        # 遍历规格信息
        for temp in specs:
            temp['sku_id'] = instance.id
            SKUSpecification.objects.create(**temp)

        return instance

    def update(self, instance, validated_data):
        specs = validated_data.pop("specs")
        # 先删除中间表数据
        SKUSpecification.objects.filter(sku_id=instance.id).delete()
        # 根据新的规格选项新建
        for temp in specs:
            temp['sku_id'] = instance.id
            SKUSpecification.objects.create(**temp)

        # 实现sku对象更新
        return super().update(instance, validated_data)


class GoodsCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = ["id", "name"]


class SPUSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPU
        fields = ["id", "name"]


class SpecsOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecificationOption
        fields = ["id", 'value']


class SPUSpecsSerializer(serializers.ModelSerializer):

    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()
    options = SpecsOptionSerializer(many=True)

    class Meta:
        model = SPUSpecification
        fields = "__all__"
