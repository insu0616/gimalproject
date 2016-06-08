from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.shop_detail, name='shop_detail'),
    url(r'^category/(?P<pk>\d+)/createcateshop$', views.shop_new, name='shop_new'),
    url(r'^createcategory/$', views.category_new, name='category_new'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url(r'^category/(?P<pk>\d+)/edit/$', views.category_edit, name='category_edit'),


]
