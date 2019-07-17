from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='attendance'
urlpatterns=[
	#url(r'^$',views.view_student,name="list"),
	url(r'^show_attendance/$',views.show_attendance,name="show_attendance"),
	url(r'^take_attendance/$',views.take_attendance,name="take_attendance"),
	url(r'^add_attendance/class/(?P<pk>[\w-]+)/$',views.add_attendance,name="add_attendance"),
	url(r'^update_attendance/class/(?P<pk>[\w-]+)/$',views.update_attendance,name="update_attendance"),
]
