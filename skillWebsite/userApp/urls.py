from django.urls import path, include
from .views import SecretarySignupView, LecturerSignupView, login_user, logout_user



urlpatterns = [

    path("signup/restau/", SecretarySignupView.as_view(), name="restau_signup"),
    path("signup/superadmin/", LecturerSignupView.as_view(), name="superAdmin_signup"),

    path("logout/", logout_user, name="logout_user" ),

    path("login/", login_user, name="login_user" ),
]
