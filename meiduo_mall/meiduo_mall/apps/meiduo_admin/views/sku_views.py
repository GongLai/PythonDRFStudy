from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from meiduo_admin.serializer.sku_serializer import *
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

    def get_serializer_class(self):
        if self.action == "categories":
            return GoodsCategoriesSerializer
        if self.action == "simple":
            return SPUSimpleSerializer
        if self.action == "specs":
            return SPUSpecsSerializer

        return self.serializer_class

    @action(methods=['get'], detail=False)
    def categories(self, request):
        cates = self.get_queryset()
        cates_serializer = self.get_serializer(cates, many=True)
        return Response(cates_serializer.data)

    @action(methods=['get'], detail=False)
    def simple(self, request):
        sim = self.get_queryset()
        sim_serializer = self.get_serializer(sim, many=True)
        return Response(sim_serializer.data)

    @action(methods=['get'], detail=False)
    def specs(self, request, pk):
        specs_qs = self.get_queryset()
        specs_serializer = self.get_serializer(specs_qs, many=True)
        return Response(specs_serializer.data)