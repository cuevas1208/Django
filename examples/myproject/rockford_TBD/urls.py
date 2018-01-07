from django.conf.urls import url

from . import views

app_name = 'rockford_TBD'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<room_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<room_id>[0-9]+)/vote2/$', views.vote2, name='vote2'),
    url(r'^open', views.open, name='open'),
    url(r'^close', views.close, name='close'),
]

