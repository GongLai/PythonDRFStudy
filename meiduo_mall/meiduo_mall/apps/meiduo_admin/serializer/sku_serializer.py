from rest_framework import serializers

from goods.models import SKU, SKUSpecification, GoodsCategory, SPU, SPUSpecification, SpecificationOption


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

    # specs = SKUSpecsSerializer(many=True)
    specs = SKUSpecsSerializer(many=True, read_only=True)

    class Meta:
        model = SKU
        fields = "__all__"


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
