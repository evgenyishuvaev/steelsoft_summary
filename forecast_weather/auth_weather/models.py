from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager



class WeatherUserManager(UserManager):
    
    def create_forecaster(self, username, email, password, **extra_fields):


        if not password:
            raise ValueError("The password must be have")


        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_forecaster", True)
        return self._create_user(username, email, password, **extra_fields)


class WeatherUser(AbstractUser):
    is_forecaster = models.BooleanField(default=False)
    objects = WeatherUserManager()
