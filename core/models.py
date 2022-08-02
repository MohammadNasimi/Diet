from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
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
    age = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

    objects = MyUserManager()

