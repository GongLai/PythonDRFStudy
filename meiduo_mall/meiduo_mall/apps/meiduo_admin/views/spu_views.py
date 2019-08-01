from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializer.spu_serializer import *
from meiduo_admin.pages import MyPage


class SPUViewSet(ModelViewSet):

    queryset = SPU.objects.all()
    serializer_class = SPUSerializer
    pagination_class = MyPage


class GoodsBrandsViewSet(ListAPIView):

    queryset = Brand.objects.all()
    serializer_class = GoodsBrandsSerializer


class GoodsCategorySerializer(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySerializer

    def get_queryset(self):

        pk = self.kwargs.get('pk', None)
        if pk:
            # 如果pk有值，说明要的是二级或三级信息
            return self.queryset.filter(parent_id=pk)

        else:
            # 如果pk为None，说明要的是一级信息
            return self.queryset.filter(parent_id=None)

