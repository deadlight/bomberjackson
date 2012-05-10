from django.db import models

# Models for the events app

class Event(models.Model):
    location = models.CharField(max_length=256)
    date = models.DateTimeField()
    url = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.location
