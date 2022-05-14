from django.db import models
from myuser.models import MyUser


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(MyUser, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']