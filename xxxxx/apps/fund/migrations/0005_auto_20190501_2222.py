# Generated by Django 2.1.7 on 2019-05-01 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0004_merge_20190430_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfund',
            name='monitor',
        ),
        migrations.AddField(
            model_name='userfund',
            name='status',
            field=models.IntegerField(choices=[(1, '拥有'), (2, '监控'), (3, '其他')], default=1),
        ),
    ]
