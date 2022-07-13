"""appLex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from appLex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.index),
    path('registro/', views.register),
    path('registra_cliente', views.registrar_cliente),
    path('ingresar', views.ingresar_app),

    #cliente
    path('inicio/', views.home_cliente),
    path('mis_solicitudes/', views.c_solicitudes),
    path('mis_contratos/', views.c_contratos),
    path('modificar_cliente/',views.modificar_cliente),
    path('modificacion_cliente/',views.modificacion_cliente),

    #abogado
    path('inicio_abogado/', views.home_abogado),
    path('causas/', views.a_causas),
    path('presupuestos/', views.a_presupuestos),
    path('detalle_presupuesto/', views.a_det_presupuesto),

    #técnico jurídico
    path('inicio_tec/', views.home_tecjuridico),
    path('solicitudes/', views.tj_solicitudes),
    path('registrar_pagos/', views.tj_registrar_pagos)
]
