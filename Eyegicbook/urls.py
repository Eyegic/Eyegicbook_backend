"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from eyegic import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^center',views.center),
    url(r'^mybook',views.mybook),
    url(r'^bbsdetail',views.bbsdetail),
    url(r'^bookdetail',views.bookdetail),
    url(r'^bbs',views.bbs),
    url(r'^context',views.context),
    url(r'^index',views.index),
    url(r'^login',views.login),
    url(r'^regist',views.register),
    url(r'^logout',views.logout),
    url(r'^book',views.bbsdetail),
    url(r'^comment',views.comment),
    url(r'^feedback',views.feedback),
    url(r'^makecomment',views.makeComment),
    url(r'^setup',views.setup),
    url(r'^subject-all',views.subject_all),
]
