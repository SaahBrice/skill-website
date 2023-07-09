from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="home" ),
    path('formation/', views.formationNormal, name="formationNormal" ),
    path('formation/', views.formationCarte, name="formationCarte" ),
]
