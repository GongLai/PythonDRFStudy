from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializer.images_serializer import *
from meiduo_admin.pages import MyPage


class ImageViewSet(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImageSerializer
    pagination_class = MyPage


class SimpleView(ListAPIView):
    queryset = SKU.objects.all()
    serializer_class = SimpleSerializer
