import re
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import jwt
from datetime  import datetime, timedelta
from django.conf import settings
# Create your models here.
CHOICES = (
    ("1", "admin"),
    ("2", "customer"),
)   
class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)
class User(AbstractUser):
    kind_user =models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = '1'
        )


    objects = MyUserManager()

    @property
    def  token(self):
        token = jwt.encode({'username':self.username , 'exp':datetime.utcnow() + timedelta(hours = 20)},
                                settings.SECRET_KEY,algorithm='HS256')

        return token