from django.shortcuts import render
from items.models import Item

# Create your views here.


def user_dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request, "dashboard/dashboard.html", {"items": items})
