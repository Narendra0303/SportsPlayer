"""project888 URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from Playerapp import views
from django.conf.urls import url


app_name='Playerapp'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.List.as_view(),name='list'),
    url(r'^detail/(?P<pk>\d+)$',views.Detail.as_view(),name='detail'),
    path('create/',views.Create.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)$',views.Update.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)$',views.Delete.as_view(),name='delete'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('signup/', views.SignUp.as_view(), name='SignUp'),

]
