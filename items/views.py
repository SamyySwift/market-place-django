from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import NewItemForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    similar_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )
    return render(
        request,
        "item-view/details.html",
        {"item": item, "similar_items": similar_items},
    )


# Create your views here.
def browse(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if query:
        items = items.filter(item_name__icontains=query)
    if category_id:
        items = items.filter(category_id=category_id)

    return render(
        request,
        "item-view/browse.html",
        {"items": items, "categories": categories, "category_id": category_id},
    )


def new_item(request):
    categories = Category.objects.all()
    form = NewItemForm()

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail-page", pk=item.id)

    return render(
        request,
        "item-view/new-item.html",
        {"form": form, "categories": categories, "title": "New Item"},
    )


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    categories = Category.objects.all()

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail-page", pk=item.id)
    else:
        form = NewItemForm(instance=item)

    return render(
        request,
        "item-view/new-item.html",
        {"form": form, "categories": categories, "title": "Edit Page"},
    )


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect("dashboard:dashboard")
