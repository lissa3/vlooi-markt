from django.db import models
from users.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    coach = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} " \
               f" coached by {self.coach}"