from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from meiduo_admin.serializer.order_serializer import *
from meiduo_admin.pages import MyPage


class OrderViewSet(ListAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSerializer
    pagination_class = MyPage

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(order_id__contains=keyword)

        return self.queryset.all()


class OrderInfoDetailView(RetrieveAPIView, UpdateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoDetailSerializer
