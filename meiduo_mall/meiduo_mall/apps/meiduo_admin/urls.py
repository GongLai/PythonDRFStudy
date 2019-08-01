from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from meiduo_admin.views.home_views import HomeView
from meiduo_admin.views.users_views import UserView
from meiduo_admin.views.sku_views import SKUViewSet
from meiduo_admin.views.spu_views import *

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户管理
    url(r'^users/$', UserView.as_view()),
    # 展示sku表信息
    url(r'^skus/$', SKUViewSet.as_view({"get": "list", "post": "create"})),
    # 修改/删除sku表信息
    url(r'^skus/(?P<pk>\d+)/$', SKUViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    url(r'^goods/$', SPUViewSet.as_view({"get": "list", "post": "create"})),
    # 获得spu信息
    url(r'^goods/simple/$', SKUViewSet.as_view({"get": "simple"})),
    # 获得可选的spu规格及选项
    url(r'^goods/(?P<pk>\d+)/specs/$', SKUViewSet.as_view({"get": "specs"})),
    # 获得spu所属的品牌信息
    url(r'^goods/brands/simple/$', GoodsBrandsViewSet.as_view()),

    # 三级分类信息
    url(r'^skus/categories/$', SKUViewSet.as_view({"get": "categories"})),

    # 展示spu所属的品牌信息
    url(r'^goods/brands/simple/$', GoodsBrandsViewSet.as_view()),
    # spu表展示一级分类
    url(r'^goods/channel/categories/$', GoodsCategorySerializer.as_view()),
    # spu表展示下级分类
    url(r'^goods/channel/categories/(?P<pk>\d+)/$',
        GoodsCategorySerializer.as_view()),
    # 修改spu表信息
    url(r'^goods/(?P<pk>\d+)/$', SPUViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # 查看/新增商品规格信息
    url(r'^goods/specs/$', SpecsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 修改/删除商品规格信息
    url(r'^goods/specs/(?P<pk>\d+)/$', SpecsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]

router = SimpleRouter()
router.register(
    prefix='statistical',
    viewset=HomeView,
    base_name='statistical')

urlpatterns += router.urls
