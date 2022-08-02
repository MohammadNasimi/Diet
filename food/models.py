from django.db import models

# Create your models here.
class food (models.Model):
    name = models.CharField(max_length=20,null=False)
    calories = models.IntegerField()
    mesure = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.name},{self.calories}'
        