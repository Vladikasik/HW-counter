from django.db import models

# Create your models here.
class HomeWork(models.Model):
    id = models.PrimaryKeyField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.IntegerField(default=0)
    expiration_date = models.DateTimeField()
    date_given = models.DateTimeField(auto_now=True)
    