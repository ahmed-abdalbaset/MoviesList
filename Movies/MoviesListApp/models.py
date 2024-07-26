from django.db import models

# Create your models here.

class Movies_Info(models.Model):
    name = models.CharField(max_length=100, help_text="This name Of the Movie")
    date = models.DateField(verbose_name="Date the movie was released")
