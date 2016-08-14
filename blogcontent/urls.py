from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^(?P<head>[0-9]+)/$',views.blog,name='blog'),
url(r'^bloglist/$',views.bloglist,name='bloglist')
]