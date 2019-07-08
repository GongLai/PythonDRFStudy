from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^book/$', views.BookView.as_view()),
    url(r'^books/$', views.BooksView.as_view()),

]