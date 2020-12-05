"""Chmura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [

    path('rejestracja/', views.rejestracja, name="rejestracja"),
	path('logowanie/', views.logowanie, name="logowanie"),  
	path('logout/', views.wylogowanie, name="logout"),


    path('', views.home, name = "home"),
    path('produkty/', views.produkty, name = "Produkty"),
    path('produkt/<str:pk>/', views.produkt, name = "produkt"),
    path('klient/<str:pk_test>', views.klient, name = "Klient"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.aktualizujZamowienie, name="update_order"),
    path('delete_order/<str:pk>', views.usunZamowienie, name="delete_order"),

]