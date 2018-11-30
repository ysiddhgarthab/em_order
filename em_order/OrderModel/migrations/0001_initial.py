# Generated by Django 2.1.2 on 2018-11-17 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('fType', models.CharField(max_length=20)),
                ('fSpicy', models.CharField(max_length=10)),
                ('fCost', models.IntegerField(max_length=10)),
                ('fDesc', models.CharField(max_length=255)),
                ('fPic', models.CharField(max_length=255)),
            ],
        ),
    ]
