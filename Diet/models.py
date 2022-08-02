import imp
from django.db import models
from core.models import User
from food.models import food
from exercise.models import exercise
# Create your models here.
class Diet(models.Model):
    user =models.ForeignKey(User, on_delete=models.RESTRICT,null=True,blank=True)
    food_Diet = models.ManyToManyField(food)
    exercise_Diet = models.ManyToManyField(exercise)

    def __str__(self):
        return f'{self.user}'   
