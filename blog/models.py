from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    info = models.CharField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.info

