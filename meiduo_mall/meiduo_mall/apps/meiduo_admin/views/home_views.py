from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
import pytz
from django.conf import settings
from datetime import timedelta

from users.models import User
from orders.models import OrderInfo


class HomeView(ViewSet):
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    @action(methods=['get'], detail=False)
    def total_count(self, request):
        """
        获取用户总数
        :param request:
        :return:
        """
        # 获取用户总数
        count = User.objects.all().count()
        # 获取当前日期
        date = timezone.now().date()

        return Response({
            'count': count,
            'date': date
        })

    @action(methods=['get'], detail=False)
    def day_increment(self, request):
        """
        获取日增用户
        :param request:
        :return:
        """
        # 1.获取当日的零时
        date_0_shanghai = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
                                                                                               second=0)

        # 2.根据零时，过滤用户
        count = User.objects.filter(date_joined__gte=date_0_shanghai).count()

        # 3.构建响应数据
        return Response({
            'count': count,
            'date': date_0_shanghai.date()
        })

<<<<<<< HEAD
    @action(methods=['get'], detail=False)
    def day_active(self, request):
        """日活跃用户"""
        # 1.获取当日零时
        date_0_shanghai = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
                                                                                               second=0)
        # print(date_0_shanghai)
        # 2.根据零时，过滤用户
        count = User.objects.filter(last_login__gte=date_0_shanghai).count()
        # print(count)

        # 3.构建响应数据
        return Response({
            'count': count,
            'date': date_0_shanghai.date()
        })
=======

>>>>>>> 19d7cb65c284fab058029fa332062a28555faef0
