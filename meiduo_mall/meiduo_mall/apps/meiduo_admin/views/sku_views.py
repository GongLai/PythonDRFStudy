from rest_framework.viewsets import ModelViewSet
from goods.models import SKU, GoodsCategory, SPU, SPUSpecification

from meiduo_admin.serializer.sku_serializer import SKUSerializer
from meiduo_admin.pages import MyPage


class SKUViewSet(ModelViewSet):

    queryset = SKU.objects.all()
    serializer_class = SKUSerializer
    pagination_class = MyPage

    def get_queryset(self):
        if self.action == "categories":
            return GoodsCategory.objects.filter(parent_id__gt=37)

        if self.action == "simple":
            return SPU.objects.all()

        if self.action == "specs":
            return SPUSpecification.objects.filter(spu_id=self.kwargs['pk'])

        keyword = self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(name__contains=keyword)
        return self.queryset.all()