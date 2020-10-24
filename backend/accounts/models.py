from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username = models.CharField(max_length=30, unique=True)
    # email = models.CharField(max_length=30, unique=True)
    # password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)

    # USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nickname', 'email', 'phone_number']
