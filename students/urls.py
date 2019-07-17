from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='students'
urlpatterns=[
	#url(r'^$',views.view_student,name="list"),
	url(r'^profile/$',views.students, name="students_profile"),
	url(r'^upload_document/$',views.simple_upload,name="upload_document"),
	url(r'^dayAttendance/$',views.dayAttendance,name="dayAttendance"),
	url(r'^monthlyAttendance/$',views.monthlyAttendance,name="monthlyAttendance"),
	url(r'^yearlyAttendance/$',views.yearlyAttendance,name="yearlyAttendance"),
	url(r'^totalAttendance/$',views.totalAttendance,name="totalAttendance"),
	url(r'^viewAttendance/$',views.viewAttendance,name='viewAttendance'),
	url(r'^Listofsubject/$',views.Listofsubject,name='Listofsubject'),
	url(r'^ListofAssignments/$',views.viewAssignment,name='Assignment'),
]
