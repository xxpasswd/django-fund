from datetime import datetime

from django.db import models

# Create your models here.
from user.models import UserProfile


class Fund(models.Model):
    code = models.CharField(max_length=10, help_text='基金code')
    name = models.CharField(max_length=30, blank=True, null=True, help_text='基金名称')
    is_valid = models.BooleanField(default=True)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '<<{}>>{}'.format(self.code, self.name)


class FundDetail(models.Model):
    code = models.ForeignKey(Fund, on_delete=models.CASCADE)
    data_time = models.DateField()
    data = models.FloatField(null=True, blank=True)


class UserFund(models.Model):
    code = models.ForeignKey(Fund, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)
    monitor = models.BooleanField(default=True)
    add_time = models.DateTimeField(default=datetime.now)
