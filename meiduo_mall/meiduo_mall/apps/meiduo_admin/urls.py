from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from meiduo_admin.views.home_views import HomeView
from meiduo_admin.views.users_views import UserView
from meiduo_admin.views.sku_views import SKUViewSet
from meiduo_admin.views.spu_views import *
from meiduo_admin.views.options_views import *
from meiduo_admin.views.channels_views import *
from meiduo_admin.views.brand_views import *
from meiduo_admin.views.images_views import *
from meiduo_admin.views.order_views import *

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户管理
    url(r'^users/$', UserView.as_view()),
    # 展示sku表信息
    url(r'^skus/$', SKUViewSet.as_view({"get": "list", "post": "create"})),
    # 修改/删除sku表信息
    url(r'^skus/(?P<pk>\d+)/$',
        SKUViewSet.as_view({"get": "retrieve",
                            "put": "update",
                            "delete": "destroy"})),

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
    url(r'^goods/(?P<pk>\d+)/$',
        SPUViewSet.as_view({"get": "retrieve",
                            "put": "update",
                            "delete": "destroy"})),

    # 查看/新增商品规格信息
    url(r'^goods/specs/$',
        SpecsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 展示/修改/删除单一商品规格信息
    url(r'^goods/specs/(?P<pk>\d+)/$',
        SpecsViewSet.as_view({"get": "retrieve",
                              "put": "update",
                              "delete": "destroy"})),
    # 展示/新增规格选项信息
    url(r'^specs/options/$',
        SpecsOptionsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 展示/修改/删除单一规格选项信息
    url(r'^specs/options/(?P<pk>\d+)/$',
        SpecsOptionsViewSet.as_view({'get': 'retrieve', "put": "update", "delete": "destroy"})),
    # 展示规格选项
    url(r'^goods/specs/simple/$', OptionSimpleViewSet.as_view()),

    # 展示频道管理数据
    url(r'^goods/channels/$',
        ChannelViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 展示修改/删除单一商品频道管理数据
    url(r'^goods/channels/(?P<pk>\d+)/$',
        ChannelViewSet.as_view({'get': 'retrieve',
                                'put': 'update',
                                'delete': 'destroy'})),
    # 展现商品频道组信息
    url(r'^goods/channel_types/$', ChannelGroupView.as_view()),
    # 展示商品频道组一级分类信息
    url(r'^goods/categories/$', GoodsCategorySerializer.as_view()),

    # 品牌管理
    # 展示/新增品牌管理数据
    url(r'^goods/brands/$', BrandViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 展示/修改/删除单一品牌管理数据
    url(r'^goods/brands/(?P<pk>\d+)/$',
        BrandViewSet.as_view({'get': 'retrieve', "put": "update", "delete": "destroy"})),

    # 图片管理
    # 展示/新增图片管理数据
    url(r'^skus/images/$', ImageViewSet.as_view({'get': 'list', 'post': 'create'})),
    # 展示/修改/删除单一图片管理数据
    url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({'get': 'retrieve', "put": "update", "delete": "destroy"})),
    # 展示图片管理SKU商品id
    url(r'^skus/simple/$', SimpleView.as_view()),

    # 订单管理
    # 获得订单多条数据
    url(r'^orders/$', OrderViewSet.as_view()),
    # 获得订单详情数据
    url(r'^orders/(?P<pk>\d+)/$', OrderInfoDetailView.as_view()),
    # 修改订单详情订单状态
    url(r'^orders/(?P<pk>\d+)/status/$', OrderInfoDetailView.as_view()),

]

router = SimpleRouter()
router.register(
    prefix='statistical',
    viewset=HomeView,
    base_name='statistical')

urlpatterns += router.urls
