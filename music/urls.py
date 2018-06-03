from django.urls import path,re_path
from . import views
app_name='music'
urlpatterns=[
    re_path(r'^$',views.index11,name='index11'),
    re_path(r'^index/$',views.index,name='index'),
    re_path(r'^index22/$',views.index22,name='index22'),
    re_path(r'^template/$',views.index3,name='index3'),
    re_path(r'^templaterender/$',views.index4,name='index4'),
    re_path(r'^songtemplate/(?P<album_id>[0-9]+)/$',views.index5,name='index5'),
    re_path(r'^(?P<album_id>[0-9]+)/$',views.index2,name='index2'),
    re_path(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite')
]