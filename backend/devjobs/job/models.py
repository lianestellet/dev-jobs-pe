from django.db import models

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=100)
    expertise = models.CharField(max_length=10)
    min_years_experience = models.IntegerField(default=0)
