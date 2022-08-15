
from django.db import models
from customer.models import customer
from food.models import food_diet_user,food_diet_admin
from exercise.models import exercise_diet_user,exercise_diet_admin
CHOICES = (
    ("1", "thin"),
    ("2", "normal"),
    ("3","fat")
)  
# Create your models here.
class Diet(models.Model):
    user =models.ForeignKey(customer, on_delete=models.RESTRICT,null=True,blank=True)
    food_Diet = models.ManyToManyField(food_diet_user)
    exercise_Diet = models.ManyToManyField(exercise_diet_user)
    kind_diet =models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = '2'
        )

    def __str__(self):
        return f'{self.user}'

 
class Diet_admin(models.Model):
    user_admin =models.ForeignKey(customer, on_delete=models.RESTRICT,null=True,blank=True)
    food_Diet_admin = models.ManyToManyField(food_diet_admin)
    exercise_Diet_admin = models.ManyToManyField(exercise_diet_admin)

    def __str__(self):
        return f'{self.user_admin}' 
