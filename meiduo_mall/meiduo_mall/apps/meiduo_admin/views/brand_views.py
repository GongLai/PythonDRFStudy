from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializer.brand_serializer import *
from meiduo_admin.pages import MyPage


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = MyPage
