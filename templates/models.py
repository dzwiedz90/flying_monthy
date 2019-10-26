from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=False)
    password = models.CharField(max_length=32, blank=False)
    email = models.CharField(max_length=64, blank=False)
    account_creation_date = models.DateTimeField(auto_now_add=True,
                                                 auto_now=False, blank=False)
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    is_staff = models.BooleanField(default=False, blank=False)
    number_of_memes = models.IntegerField(default=0, blank=False)
