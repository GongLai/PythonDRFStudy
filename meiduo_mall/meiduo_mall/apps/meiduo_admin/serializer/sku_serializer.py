from rest_framework import serializers

from goods.models import SKU, SKUSpecification


class SKUSpecsSerializer(serializers.ModelSerializer):
    # "spec_id": "规格id",
    # "option_id": "选项id"
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
