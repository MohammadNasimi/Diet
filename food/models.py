from operator import mod
from statistics import mode
from django.db import models
from customer.models import customer
# Create your models here.
class food (models.Model):
    name = models.CharField(max_length=20,null=False)
    calories = models.IntegerField()
    mesure = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.name},{self.calories}'
        
class food_diet_user(models.Model):
    customer_food = models.ForeignKey(customer, on_delete=models.RESTRICT)
    food_field = models.ForeignKey(food,on_delete=models.RESTRICT)
    mesure_food_customer = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.food_field},{self.mesure_food_customer}'