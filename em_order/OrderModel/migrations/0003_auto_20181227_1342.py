# Generated by Django 2.1.4 on 2018-12-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderModel', '0002_userprofile_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='eId',
            field=models.CharField(max_length=30, unique=True, verbose_name='employee_id'),
        ),
    ]
