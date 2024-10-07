from django.urls import path
import auth_system.views as views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
]