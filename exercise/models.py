from django.db import models

from customer.models import customer
# Create your models here.
class exercise (models.Model):
    name_exercise = models.CharField(max_length=20,null=False)
    calories = models.IntegerField()
    time = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name_exercise}'

class exercise_diet_user(models.Model):
    customer_exercise = models.ForeignKey(customer, on_delete=models.RESTRICT)
    exersise_field = models.ForeignKey(exercise,on_delete=models.RESTRICT)
    time_exercise_customer = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.customer_exercise}{self.time_exercise_customer}'