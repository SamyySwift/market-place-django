from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("category_name",)

        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.category_name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    item_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.item_name
