"""
URL configuration for project1 project.

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
from django.urls import path
from home import views as v1
from about import views as v2
from dashboard import views as v3
from data import views as v4
from login import views as v5
from services import views as v6
from signup import views as v7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.home,name="home"),
    path('about/',v2.about,name="about"),
    path('dashboard/',v3.dashboard,name="dashboard"),
    path('data/',v4.data,name="data"),
    path('login/',v5.login,name="login"),
    path('logout/',v5.login,name="logout"),
    path('services/',v6.services,name="services"),
    path('signip/',v7.signup,name="signup"),
    path('update/<int:id>',v7.update,name="update"),
    path('delete/<int:id>',v7.delete,name="delete"),
]
