"""
URL configuration for shyftlabs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .shyftuser import views as userview
from .shyftcourse import views as courseview
from .shyftresults import views as resultview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', userview.getUser),
    path('alluser/', userview.getAllUser),
    path('deleteuser/', userview.deleteUser),
    path('course/', courseview.course),
    path('allcourse/', courseview.allcourse),
    path('deletecourse/', courseview.deleteCourse),
    path('result/', resultview.result),
    path('allresult/', resultview.getAllResults),
    path('deleteresult/', resultview.deleteResult),
]
