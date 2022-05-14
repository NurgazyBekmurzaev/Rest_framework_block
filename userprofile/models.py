from django.db import models
from myuser.models import MyUser


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='user_profile')

    avatar = models.ImageField(upload_to='posts', blank=True, null=True)
    bio = models.TextField()

    def str(self):
        return self.user.email