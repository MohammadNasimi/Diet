
from django.db import models
from core.models import User
from food.models import food_diet_user
from exercise.models import exercise_diet_user
# Create your models here.
class Diet(models.Model):
    user =models.ForeignKey(User, on_delete=models.RESTRICT,null=True,blank=True)
    food_Diet = models.ManyToManyField(food_diet_user)
    exercise_Diet = models.ManyToManyField(exercise_diet_user)

    def __str__(self):
        return f'{self.user}'   
