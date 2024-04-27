from django.db import models
from datetime import datetime

# Create your models here.
class Blog (models.Model):
    title = models.CharField (max_length = 100)
    articles = models.CharField(max_length = 2000)
    created_when = models.DateTimeField(default = datetime.now, blank = True)
    
# class About(models.Model):
#     words = models.CharField (max_length = 100)