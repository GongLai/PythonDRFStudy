from rest_framework.viewsets import ViewSet
from django.utils import timezone
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from users.models import User


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

        return JsonResponse({
            'count': count,
            'date': date
        })

