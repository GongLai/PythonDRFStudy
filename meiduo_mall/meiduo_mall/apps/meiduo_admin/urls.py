from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from .views.home_views import HomeView

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),

]

router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeView, base_name='statistical')

urlpatterns += router.urls
