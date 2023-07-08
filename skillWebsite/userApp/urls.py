from django.urls import path, include
from . import views



urlpatterns = [
    path('skillLogin/', views.login, name="skill_login" ),
]
