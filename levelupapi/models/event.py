from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    hoster = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.DO_NOTHING)
    datetime = models.CharField(max_length=50)
    attendees = models.ManyToManyField("Gamer", through="GamerEvent", related_name="gamer_event")