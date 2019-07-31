from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from .views.home_views import HomeView
from .views.users_views import UserView
from .views.sku_views import SKUViewSet
from .views.spu_views import SPUViewSet

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户管理
    url(r'^users/$', UserView.as_view()),
    # 展示sku表信息
    url(r'^skus/$', SKUViewSet.as_view({"get": "list", "post": "create"})),
    # 修改/删除sku表信息
    url(r'^skus/(?P<pk>\d+)/$', SKUViewSet.as_view({"get": "retrieve",
                                                    "put": "update",
                                                    "delete": "destroy"})),

    # 获得spu信息
    url(r'^goods/simple/$', SKUViewSet.as_view({"get": "simple"})),
    # 获得可选的spu规格及选项
    url(r'^goods/(?P<pk>\d+)/specs/$', SKUViewSet.as_view({"get": "specs"})),

    # 三级分类信息
    url(r'^skus/categories/$', SKUViewSet.as_view({"get": "categories"})),


    url(r'^goods/$', SPUViewSet.as_view({"get": "list"})),


]

router = SimpleRouter()
router.register(
    prefix='statistical',
    viewset=HomeView,
    base_name='statistical')

urlpatterns += router.urls
