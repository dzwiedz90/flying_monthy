from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comments(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey(Post, related_name='comment',
                             on_delete=models.CASCADE)
