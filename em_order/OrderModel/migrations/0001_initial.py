# Generated by Django 2.1.4 on 2018-12-18 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20, unique=True)),
                ('fType', models.CharField(max_length=20)),
                ('fSpicy', models.CharField(max_length=10)),
                ('fCost', models.IntegerField(blank=True, null=True)),
                ('fDesc', models.CharField(blank=True, max_length=255, null=True)),
                ('fPic', models.ImageField(blank=True, null=True, upload_to='OrderMedel/')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mDate', models.DateField(unique=True)),
                ('bre', models.CharField(max_length=255)),
                ('lun', models.CharField(max_length=255)),
                ('din', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eId', models.CharField(max_length=50)),
                ('oDate', models.DateField()),
                ('bre', models.BooleanField()),
                ('lun', models.BooleanField()),
                ('din', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('sDate', models.DateField()),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eName', models.CharField(max_length=30, verbose_name='employee_name')),
                ('flag', models.IntegerField(verbose_name='flag')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
