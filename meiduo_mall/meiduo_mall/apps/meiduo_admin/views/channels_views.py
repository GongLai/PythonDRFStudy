from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializer.channels_serializer import *
from meiduo_admin.pages import MyPage


class ChannelViewSet(ModelViewSet):
    queryset = GoodsChannel.objects.all()
    serializer_class = ChannelSerializer
    pagination_class = MyPage


class ChannelGroupView(ListAPIView):
    queryset = GoodsChannelGroup.objects.all()
    serializer_class = ChannelGroupSerializer
