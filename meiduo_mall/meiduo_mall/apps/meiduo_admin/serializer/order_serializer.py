from rest_framework import serializers

from orders.models import OrderInfo, OrderGoods
from goods.models import SKU


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = ['order_id', 'create_time']


class SKUSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ['name', 'default_image']


class OrderGoodsSerializer(serializers.ModelSerializer):
    sku = SKUSimpleSerializer()

    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']


class OrderInfoDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    skus = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'

