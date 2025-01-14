from django.db import models
from django.contrib.auth.models import User



    
class MetronomeSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    range = models.PositiveIntegerField(default=100)  # Темп в ударах в минуту
    counter_bottom = models.PositiveIntegerField(default=4)
    counter_top = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"{self.name} - {self.user.username}"
    
