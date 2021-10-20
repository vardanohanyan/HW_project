from django.db import models
# Problem 1
#
# Create a Human model. It has name, surname, year_of_birth, and gender (can be Male or Female).
# Create a migration and syncronize with the db.

class Human(models.Model):
    gench = (
        ('m', 'male'),
        ('f', 'female')
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    yb = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gench)
