from rest_framework.generics import ListAPIView, CreateAPIView

from users.models import User
from meiduo_admin.serializer.users_serializer import UserSerializer
from meiduo_admin.pages import MyPage


class UserView(ListAPIView, CreateAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
    pagination_class = MyPage

    def get_queryset(self):
        """
        根据字符串参数keyword过滤
        :return: 过滤后的数据集
        """

        keyword = self.request.query_params.get('keyword')
        # 如果请求字符串参数中有keyword，过滤（名字以keyword开头）
        if keyword:
            return self.queryset.filter(username__startswith=keyword)
        # 如果没有keyword，返回默认处理的数据集
        return self.queryset.all()  # QuerySet： 1、惰性执行  2、缓存

