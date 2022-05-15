from django.db import models

from auth_user.models import User
# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
