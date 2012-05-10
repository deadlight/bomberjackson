from django.db import models

# Models for the reviews app

class Review(models.Model):
    reviewer = models.CharField(max_length=256)
    date = models.DateTimeField()
    url = models.CharField(max_length=1024, null=True, blank=True)
    quote = models.TextField()

    def __unicode__(self):
        return self.reviewer
