from rest_framework import serializers

<<<<<<< HEAD
from goods.models import SPU, Brand
=======
from goods.models import SPU, Brand, GoodsCategory
>>>>>>> dev


class SPUSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
<<<<<<< HEAD
        fields = '__all__'


class GoodsBrandsSerializer(serializers.ModelSerializer):
=======
        # fields = '__all__'
        exclude = ['category1', 'category2', 'category3']


class BrandSerializer(serializers.ModelSerializer):
>>>>>>> dev

    class Meta:
        model = Brand
        fields = ['id', 'name']
<<<<<<< HEAD
=======


class GoodsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']
>>>>>>> dev
