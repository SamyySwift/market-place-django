from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("<int:pk>/", views.detail_view, name="detail-page"),
    path("new-item", views.new_item, name="new-item"),
    path("delete/<int:pk>", views.delete_item, name="delete"),
    path("edit/<int:pk>/", views.edit_item, name="edit"),
    path("browse", views.browse, name="browse"),
]
