# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from OrderModel.models import UserProfile
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def register(request):
	if request.method == 'POST':
		eId = request.POST['eId']
		username = request.POST['username']
		password = request.POST['password2']
		flag = request.POST['flag']
		# 使用内置User自带create_user方法创建用户，不需要使用save()
		user = User.objects.create_user(username=username, password=password)
		# 如果直接使用objects.create()方法后不需要使用save()
		user_profile = UserProfile(user=user,eId=eId,flag=flag)
		user_profile.save()
		return HttpResponseRedirect("/login")

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
			request.session['username'] = user.username
			userProfile = UserProfile.objects.filter(user=user)
			#登录成功之后设置session
			for u in userProfile:
				request.session['eId'] = u.eId
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

@login_required 
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def userAdmin(request):
	return render(request,"userAdmin.html")