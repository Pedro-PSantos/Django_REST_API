from django.db import models


#What the drink should look like
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # How the drink should be displayed
    def __str__(self):
        return self.name + " - " + self.description