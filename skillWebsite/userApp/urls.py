from django.urls import path, include
from .views import SecretarySignupView, LecturerSignupView, login_user, logout_user



urlpatterns = [

    path("signup/secretary/", SecretarySignupView.as_view(), name="secretary_signup"),
    path("signup/lecturer/", LecturerSignupView.as_view(), name="lecturer_signup"),

    path("logout/", logout_user, name="logout_user" ),

    path("login/", login_user, name="login_user" ),
]
