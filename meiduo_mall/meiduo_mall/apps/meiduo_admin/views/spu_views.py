from rest_framework.viewsets import ModelViewSet

from goods.models import SPU
from meiduo_admin.serializer.spu_serializer import SPUSerializer
from meiduo_admin.pages import MyPage


class SPUViewSet(ModelViewSet):

    queryset = SPU.objects.all()
    serializer_class = SPUSerializer
    pagination_class = MyPage


