from django.db import models

# imports for token (REST API)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# we have to put this code to other app !!!
class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.user.username} Profile'
