from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("home", views.index, name="home"),
    path("contact", views.contact, name="contact-page"),
    path("signup", views.signup, name="signup-page"),
    path("login", views.login_page, name="login-page"),
    path("logout", views.logout_page, name="logout-page"),
    path("delete", views.delete_account, name="delete-account"),
    path("update-profile", views.update_user, name="update-profile"),
]
