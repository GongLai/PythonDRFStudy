from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializer.perm_serializer import *
from meiduo_admin.pages import MyPage


class PermViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermSerializer
    pagination_class = MyPage


class ContentTypeViewSet(ListAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = MyPage


class GroupPermView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermSerializer
