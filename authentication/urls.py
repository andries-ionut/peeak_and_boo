"""
URL configuration for peeak_and_boo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(),name='login'),
    path('logout/', LogOutUserView.as_view(), name='logout'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('password-cahnge/', UserChangePasswordView.as_view(), name='password-change'),
]
