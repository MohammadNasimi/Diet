from django.db import models

# Create your models here.
class exercise (models.Model):
    name_exercise = models.CharField(max_length=20,null=False)
    calories = models.IntegerField()
    time = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name_exercise}'