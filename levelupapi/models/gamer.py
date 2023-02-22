from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):
    #creates a 1 to 1 relation with the user and gamer
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'