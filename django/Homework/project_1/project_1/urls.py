"""
URL configuration for project_1 project.

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
from about import views as v1
from dashboard import views as v2
from home import views as v3
from login import views as v4
from registration import views as v5
from update import views as v6
from view import views as v7


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',v1.about,name="about"),
    path('dashboard/',v2.dashboard,name="dashboard"),
    path('logout/',v2.logout,name="logout"),
    path('',v3.home,name="home"),
    path('login/',v4.login,name="login"),
    path('registration/',v5.registration,name="registration"),
    path('update/<int:id>/',v6.update,name="update"),
    path('delete/<int:id>/',v6.delete,name="delete"),
    path('view/',v7.view,name="view"),
]
