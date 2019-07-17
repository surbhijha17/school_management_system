from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='teachers'
urlpatterns=[
	#url(r'^$',views.view_student,name="list"),
	url(r'^$',views.teacher_profile,name="profile"),
	url(r'^class/$',views.classes,name="classes"),
	url(r'^upload_assignment/$',views.upload_assignment, name="assignment"),
	url(r'^uploaded_assignment/$',views.uploaded_assignment, name="uploaded_assignment"),
]
