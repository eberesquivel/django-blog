from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_lista, name='post_lista'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detalle, name='post_detalle'),
    url(r'^post/nuevo/$', views.post_new, name='nuevo_post'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.post_editar, name='post_editar'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publicar/$', views.post_publicar, name='post_publicar'),
    url(r'^post/(?P<pk>\d+)/remover/$', views.post_remover, name='post_remover'),



]