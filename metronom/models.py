from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    
    range = models.IntegerField()  # Измените тип поля на подходящий, если необходимо
    counter_bottom = models.IntegerField()
    counter_top = models.IntegerField()

    def __str__(self):
        return f"Username: {self.username}, Range: {self.range}, Counter Bottom: {self.counter_bottom}, Counter Top: {self.counter_top}"