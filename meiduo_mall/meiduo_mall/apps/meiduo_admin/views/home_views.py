from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
import pytz
from django.conf import settings
from datetime import timedelta

from users.models import User
from meiduo_admin.serializer.home_serializer import GoodsDaySerializer
from goods.models import GoodsVisitCount


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

    @action(methods=['get'], detail=False)
    def day_orders(self, request):
        """日下单用户"""
        # 1.获取当日零时
        date_0_shanghai = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
                                                                                               second=0)
        # 2.根据零时，过滤用户
        user_qs = User.objects.filter(orders__create_time__gte=date_0_shanghai)
        count = len(set(user_qs))
        # 3.构建响应数据
        return Response({
            'count': count,
            'date': date_0_shanghai.date()
        })

    @action(methods=['get'], detail=False)
    def month_increment(self, request):
        """月增用户"""
        # 1.获取当日零时
        date_0_shanghai = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
                                                                                               second=0)
        # 2.获得当日日期
        cur_date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE))
        start_date = cur_date - timedelta(days=29)

        date_list = []
        for index in range(30):
            # 每遍历一次，获得一个当日的日期
            # index = 0
            clac_date = (start_date + timedelta(days=index)).replace(hour=0, minute=0, second=0)

            # 过滤用户
            count = User.objects.filter(date_joined__gte=clac_date,
                                        date_joined__lt=clac_date + timedelta(days=1)).count()

            date_list.append({
                "count": count,
                "date": clac_date.date()
            })

        return Response(date_list)

    @action(methods=['get'], detail=False)
    def goods_day_views(self, request):
        """日分类商品访问量统计"""
        # 1.获得序列化数据GoodsVisitCount
        date_0_shanghai = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
                                                                                               second=0)
        gv = GoodsVisitCount.objects.filter(create_time__gte=date_0_shanghai)

        # 2.调用序列化器完成序列化数据
        gvs = GoodsDaySerializer(gv, many=True)

        # 3.构建响应对象
        return Response(gvs.data)
