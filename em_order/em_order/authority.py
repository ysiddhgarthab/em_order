# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from OrderModel.models import UserProfile
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



def register(request):
	if request.method == 'POST':
		eId = request.POST['eId']
		eName = request.POST['eName']
		password = request.POST['password2']
		flag = request.POST['flag']
		# 使用内置User自带create_user方法创建用户，不需要使用save()
		user = User.objects.create_user(username=eId, password=password)
		# 如果直接使用objects.create()方法后不需要使用save()
		user_profile = UserProfile(user=user,eName=eName,flag=flag)
		user_profile.save()
	return render(request,"register.html")


def login(request):
	#获取用户下一跳地址，如果没有赋值为一个空字符串
	next = request.GET.get('next','')
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			request.session['id'] = user.id
			request.session['eId'] = user.username
			userProfile = UserProfile.objects.filter(user=user)
			#登录成功之后设置session
			for u in userProfile:
				request.session['eName'] = u.eName
				request.session['flag'] = u.flag
			#登录成功之后如果有下一跳地址则跳转到目的地址
			if request.POST['next']:
				return HttpResponseRedirect(request.POST['next'])
			else:
				return HttpResponseRedirect("/")
		else:
			# 登陆失败
			message = "登录失败，请检查输入的用户名或密码是否正确"
			return render(request, 'login.html',{"message":message})
	return render(request, 'login.html',{"next":next})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


@login_required
def userAdmin(request):
	if request.POST:
		keyWord = request.POST['keyWord']
		userResult = User.objects.filter(username__icontains=keyWord)
		userList = []
		for u in userResult:
			user = []
			userProfile = UserProfile.objects.filter(user=u)
			user.append(u.id)
			user.append(u.username)	
			user.append(userProfile[0].eName)
			user.append(userProfile[0].flag)
			userList.append(user)
		return render(request,"userAdmin.html",{"userList":userList})

	allUser = User.objects.all()
	userList = []
	for u in allUser:
		user = []
		userProfile = UserProfile.objects.filter(user=u)
		user.append(u.id)
		user.append(u.username)	
		user.append(userProfile[0].eName)
		user.append(userProfile[0].flag)
		userList.append(user)
	return render(request,"userAdmin.html",{"userList":userList})


@login_required
def del_user(request):
	if request.GET:
		userId = request.GET['id']
		User.objects.filter(id=userId).delete()
	return HttpResponseRedirect("/userAdmin")


@login_required
def edit_user(request):
	if request.GET:
		userInfo = {}
		userInfo["id"]=request.GET['id']
		userInfo["eId"]=request.GET['eId']
		userInfo["eName"]=request.GET['eName']
		userInfo["flag"]=request.GET['flag']
		return render(request,"edit_user.html",{"userInfo":userInfo})
	if request.POST:
		userId = request.POST['userId']
		eId = request.POST['eId']
		eName = request.POST['eName']
		password = request.POST['password']
		flag = request.POST['flag']
		user = User.objects.filter(id=userId)[0]
		user.username = eId
		if password:
			user.set_password(password)
		user.save()
		UserProfile.objects.filter(user_id=userId).update(eName=eName,flag=flag)
		return HttpResponseRedirect("/userAdmin")


@login_required
def change_password(request):
	if request.POST:
		username = request.session['eId']
		password = request.POST['cur_pwd']
		user = auth.authenticate(username=username, password=password)
		new_pwd1 = request.POST['new_pwd1']
		new_pwd2 = request.POST['new_pwd2']
		if user is None or user.is_active == 0:
			return render(request,"change_password.html",{"message":"原密码不正确！"})
		user.set_password(new_pwd2)
		user.save()
		return HttpResponseRedirect("/login")
	return render(request,"change_password.html")