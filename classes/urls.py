from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='classes'
urlpatterns=[
	url(r'^(?P<pk>[\w-]+)/student/$',views.show_byclass,name="stubyclass"),
]
