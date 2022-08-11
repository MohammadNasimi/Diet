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

class food_diet_admin(models.Model):
    admin_food = models.ForeignKey(customer, on_delete=models.RESTRICT)
    food_field_admin = models.ForeignKey(food,on_delete=models.RESTRICT)
    mesure_food_admin = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.food_field_admin},{self.mesure_food_admin}'