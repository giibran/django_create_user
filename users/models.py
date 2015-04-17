from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    def __str__(self):
        return '{username}'.format(username=self.username)
