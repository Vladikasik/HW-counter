from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class HomeWork(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    task_file = models.URLField()
    priority = models.IntegerField(default=0)
    date_given = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField()
    result_in_system = models.BooleanField(default=False)
    link_to_result = models.URLField()
    result_text = models.TextField()
