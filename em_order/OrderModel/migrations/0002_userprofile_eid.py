# Generated by Django 2.1.4 on 2018-12-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='eId',
            field=models.CharField(default=1, max_length=30, verbose_name='employee_id'),
            preserve_default=False,
        ),
    ]
