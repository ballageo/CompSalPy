from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test/(?P<st1>\w+)/(?P<st2>\w+)$', views.test),
    url(r'^test2/(?P<st1>\w+)/(?P<st2>\w+)$', views.test2),
    url(r'^color/(?P<c1>\w+)$', views.color),
]