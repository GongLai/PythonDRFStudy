from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializer.admin_serializer import *
from meiduo_admin.pages import MyPage
from meiduo_admin.serializer.perm_serializer import *


class AdminViewSet(ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    pagination_class = MyPage


class GroupSimpleView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
