"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import login_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$',views.home),
    url(r'^about/$',views.about,name="about"),
    url(r'^curriculum/$',views.curriculum,name="curriculum"),
    url(r'^attendance/',include('attendance.urls')),
    url(r'^exam/',include('exams.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^teachers/',include('teachers.urls')),
    url(r'^class/',include('classes.urls')),
	url(r'^accounts/',include('accounts.urls')),
    url(r'^students/',include('students.urls')),
    url(r'^admission/',include('admission.urls')),
    url(r'^fee/',include('fee.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
