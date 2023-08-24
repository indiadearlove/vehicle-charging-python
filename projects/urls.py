"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

from projects.charge.views import vehicle_list, vehicle_detail, stop_charge, start_charge
from projects.company.views import company_list, company_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/company/$', company_list),
    re_path(r'^api/company/([0-9])$', company_detail),
    re_path(r'^api/vehicle/$', vehicle_list),
    re_path(r'^api/vehicle/([0-9])$', vehicle_detail),
    re_path(r'^api/stop_vehicle_charge/([0-9])$', stop_charge),
    re_path(r'^api/start_vehicle_charge/([0-9])$', start_charge),
]
