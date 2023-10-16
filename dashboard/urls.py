from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("user-dashboard", views.user_dashboard, name="dashboard"),
]
