from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True, error_messages={'unique': 'This field must be unique.'})
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
