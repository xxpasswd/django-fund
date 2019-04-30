from datetime import datetime

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    is_display = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=True)
    add_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)
