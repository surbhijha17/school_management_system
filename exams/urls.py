from django.conf.urls import url
from .views import *
from exams import views

app_name = 'exams'

urlpatterns=[
    url(r'^$', views.Exams, name = 'AllSubject'),
    url(r'^(?P<examname>[\w-]+)/(?P<tname>[\w-]+)$', views.level, name = 'AllLevel'),
    url(r'^(?P<examname>[\w-]+)$', views.Topics, name = 'AllTopic'),
    url(r'^(?P<examname>[\w-]+)/(?P<tname>[\w-]+)/Level/(?P<value>\d+)$', views.question, name = 'Ques'),
    url(r'^(?P<examname>[\w-]+)/(?P<tname>[\w-]+)/Level/(?P<value>\d+)/start$', views.starttest, name = 'StartTest'),
    #url(r'^subject/topic/level/checkout/(?P<pk>\d+)$', views.checkout, name="Checkout"),
    #url(r'^handlerequest/$', views.handlerequest, name="HandleRequest"),
]
