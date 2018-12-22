from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Food(models.Model):
	fName  = models.CharField(max_length=20,unique=True)
	fType  = models.CharField(max_length=20)
	fSpicy = models.CharField(max_length=10)
	fCost  = models.IntegerField(null=True,blank=True) 
	fDesc  = models.CharField(max_length=255,null=True,blank=True)
	fPic   = models.ImageField(upload_to='OrderMedel/',null=True,blank=True)


class Menu(models.Model):
	mDate  = models.DateField(unique=True)
	bre    = models.CharField(max_length=255)
	lun    = models.CharField(max_length=255)
	din    = models.CharField(max_length=255)


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	eId = models.CharField(
 			'employee_id',
 			max_length=30
 		)
	eName = models.CharField(
 			'employee_name',
 			max_length=30
 		)
	flag = models.IntegerField('flag')

	# class Meta:
	# 	verbose_name = 'User Profile'

	# def __str__(self):
	# 	return self.user.__str__()


class Order(models.Model):
	eId   = models.CharField(max_length=50)
	oDate = models.DateField()
	bre   = models.BooleanField()
	lun   = models.BooleanField()
	din   = models.BooleanField()


class Score(models.Model):
	fName = models.CharField(max_length=50)
	score = models.IntegerField()
	sDate = models.DateField()
	comment = models.CharField(max_length=255,null=True,blank=True)
	user_id = models.IntegerField()
