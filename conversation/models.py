# from django.db import models
# from items.models import Item
# from django.contrib.auth.models import User


# # Create your models here.
# class Conversation(models.Model):
#     item = models.ForeignKey(
#         Item, related_name="conversations", on_delete=models.CASCADE
#     )
#     members = models.ManyToManyField(User, related_name="conversations")
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["-modified_at"]


# class ConversationMessages(models.Model):
#     conversation = models.ForeignKey(
#         Conversation, related_name="messages", on_delete=models.CASCADE
#     )
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
