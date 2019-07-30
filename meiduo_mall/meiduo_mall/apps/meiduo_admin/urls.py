from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from .views.home_views import HomeView
from .views.users_views import UserView
from .views.sku_views import SKUViewSet

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户管理
    url(r'^users/$', UserView.as_view()),

    url(r'^skus/$', SKUViewSet.as_view({"get": "list"})),

]

router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeView, base_name='statistical')

urlpatterns += router.urls
