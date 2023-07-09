from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="home" ),
    path('home', views.userHome, name="user_home" ),
    path('formation/', views.formationNormal, name="formationNormal" ),
    path('formation/', views.formationCarte, name="formationCarte" ),
]
