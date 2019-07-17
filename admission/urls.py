from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='admission'
urlpatterns=[
	#url(r'^$',views.view_student,name="list"),
	url(r'^inquiry/$',views.inquiry,name="inquiry"),
	url(r'^registeration/$',views.Registeration,name="registeration"),

]
