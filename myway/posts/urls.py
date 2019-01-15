from django.conf.urls import url, include
from . import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
  url(r'post_detail', views.get_post_detail_view, name='post_details'),
  url(r'^create', views.post_create_view, name='create')
];