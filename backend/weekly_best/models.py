from django.db import models

# Create your models here.
class WeeklyBest(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='weekly_best/')

    def __str__(self):
        return self.title