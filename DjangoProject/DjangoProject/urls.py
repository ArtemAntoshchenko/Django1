"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,re_path
from newProject import views

urlpatterns = [
    # re_path(r'^product/(?P<id>\d+)',views.products),
    # path('product/<path:id>',views.products),
    path('product/<int:id>',views.products),
    path('greeting/<str:name>/<str:language>', views.greeting),
    path('greeting/<str:name>', views.greeting),
    path('', views.home_view, name='home'),
    re_path(r'^profile/(?P<username>\D+)/post/(?P<post_id>\d+)',views.profile),
]
