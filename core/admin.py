from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # fields = ["username"]
    inlines = [ProfileInline]


# # Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
