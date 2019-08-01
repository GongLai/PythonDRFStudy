from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializer.options_serializer import *
from meiduo_admin.pages import MyPage


class SpecsOptionsViewSet(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = SpecsOptionsSerializer
    pagination_class = MyPage

    def get_queryset(self):
        keyword = self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(name__contains=keyword)
        return self.queryset.all()


class OptionSimpleViewSet(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = OptionSimpleSerializer
