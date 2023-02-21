from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    game_type = models.ForeignKey("GameType", on_delete=models.DO_NOTHING)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=50)
