from django.conf.urls import url
from django.contrib import admin
from .import views
from .views import *
app_name='fee'
urlpatterns=[
	#url(r'^$',views.view_student,name="list"),
	url(r'^payment/$',views.fee, name="payment"),
    url(r'^handlerequest/$', views.handlerequest, name="HandleRequest"),
	url(r'^pdf/(?P<pk>\d+)/$',views.GeneratePdf,name="pdf"),
	url(r'^error/$',views.acess, name="error"),
]
