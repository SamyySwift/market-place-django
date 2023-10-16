from django.shortcuts import render, redirect, get_object_or_404
from items.models import Category, Item
from .forms import SignupForm, ProfileForm
from core.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(
        request,
        "core/index.html",
        {"categories": categories, "items": items},
    )


def contact(request):
    return render(request, "core/contact.html", {})


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, "core/profile.html", {"profile": profile})


def signup(request):
    form = SignupForm()
    message = ""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Account created successfully!"
            return redirect("core:login-page")

    return render(request, "core/signup.html", {"form": form, "message": message})


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:home")
        else:
            return render(request, "core/login.html")

    return render(request, "core/login.html")


def logout_page(request):
    logout(request)
    return redirect("core:login-page")


@login_required
def update_user(request):
    current_user = User.objects.get(id=request.user.id)
    current_profile = Profile.objects.get(user__id=request.user.id)

    user_form = SignupForm(
        request.POST or None, request.FILES or None, instance=current_user
    )
    profile_form = ProfileForm(
        request.POST or None, request.FILES or None, instance=current_profile
    )
    print(user_form)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        login(request, current_user)
        # return redirect("core:home")

    return render(
        request,
        "core/update_user.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


@login_required
def delete_account(request):
    current_user = User.objects.get(id=request.user.id)
    current_user.delete()
    return redirect("core:home")
