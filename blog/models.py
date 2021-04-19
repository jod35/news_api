from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=False)
    content = models.TextField(null=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
