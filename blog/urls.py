from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detalle, name='post_detalle'),
    url(r'^post/nuevo/$', views.post_new, name='nuevo_post'),
]