"""
URL configuration for mysite project.

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
from django.urls import path
from webapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index),
    path("info/",info),
    path("crud_index",crud_index,name="crud_index"),
    path("crud_create",crud_create,name="crud_create"),
    path("crud_store",crud_store,name="crud_store"),
    path("crud_edit/<int:id>",crud_edit,name="crud_edit"),
    path("crud_update/<int:id>",crud_update,name="crud_update"),
    path("crud_delete/<int:id>",crud_delete,name="crud_delete"),
]
