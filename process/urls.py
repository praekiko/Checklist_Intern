from django.conf.urls import url

from . import views

app_name = 'process'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),    
    url(r'^(?P<pk>[0-9]+)/$', views.reportDetail.as_view(), name='reportDetail'),    
    url(r'^(?P<pk>[0-9]+)/stage/$', views.stageDetail.as_view(), name='stageDetail'),
]