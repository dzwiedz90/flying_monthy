from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, default=None, null=True, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
