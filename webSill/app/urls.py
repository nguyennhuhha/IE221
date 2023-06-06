from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.home, name="home"),
    path('2D/',views.TwoD,name="2D"),
    path('3D/',views.ThreeD,name="3D"),
    path('Icon/',views.Icon,name="Icon"),
    path('About/',views.About,name="About"),
]
