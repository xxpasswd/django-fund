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
    FUND_CHOICE = (
        (1, '拥有'),
        (2, '监控'),
        (3, '其他')
    )
    code = models.OneToOneField(Fund, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.IntegerField(default=1, choices=FUND_CHOICE)
    is_valid = models.BooleanField(default=True)
    add_time = models.DateTimeField(default=datetime.now)
