"""minor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from facelook import views
urlpatterns = [
    path('admin1/',views.admin1),
    path('file1/',views.file1),
    path('adduser/',views.adduser,name = 'adduser'),
    path('adduser1/',views.adduser1,name='adduser1'),
    path('emplogin/',views.emplogin,name='login'),
    path('live/',views.live),
    path('emplogin1/',views.emplogin1),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('admin2/',views.admin2,name='admin2'),

]
