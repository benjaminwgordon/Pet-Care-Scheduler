from django.db import models

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=75)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}: {self.meal}"

