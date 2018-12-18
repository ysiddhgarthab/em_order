# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from OrderModel.models import Menu,Food
from django.http import HttpResponse,HttpResponseRedirect
import json
import time
from django.contrib.auth.decorators import login_required


def show_menu(request):
	if request.POST:
		startDate = request.POST['startDate'] or '1969-01-01'
		stopDate   = request.POST['stopDate'] or '2100-01-01'
		rMenu = Menu.objects.filter(mDate__range=(startDate,stopDate))
		for i in rMenu:
			i.bre = i.bre.split(",")
			i.lun = i.lun.split(",")
			i.din = i.din.split(",")
		return render(request, 'index.html', {'menu':rMenu})
	else:
		message = request.GET.get("message",'')
		today = time.strftime('%Y-%m-%d',time.localtime())
		rMenu = Menu.objects.filter(mDate=today)
		for i in rMenu:
			i.bre = i.bre.split(",")
			i.lun = i.lun.split(",")
			i.din = i.din.split(",")
		return render(request, 'index.html', {'menu':rMenu,'message':message})


# 获得所有的菜品名称返回添加菜单页面，初始化下拉框
@login_required
def add_menu(request):
	allFood = Food.objects.values("fName")
	message = request.GET.get('message','')
	fList = []
	for n in allFood:
		fList.append(n)
	return render(request,'add_menu.html',{"allFood":json.dumps(fList),"message":message})


@login_required
def add_menu_check(request):
	if request.POST:
		mDate  = request.POST['mDate']
		today = time.strftime('%Y-%m-%d',time.localtime())
		if mDate<=today:
			return HttpResponseRedirect("/add_menu?message=请选择大于今天的日期！")
		if Menu.objects.filter(mDate=mDate):
			return HttpResponseRedirect("/add_menu?message=该日期的菜单已存在！")
		bre    = request.POST['bre']
		lun    = request.POST['lun']
		din    = request.POST['din']

	me = Menu(mDate=mDate,bre=bre,lun=lun,din=din)
	me.save()
	return HttpResponseRedirect("/add_menu")


@login_required
def edit_menu(request):
	if request.GET:
		# 获得所提交日期对应的菜单数据
		mDate = request.GET['mDate']
		thisMenu = Menu.objects.filter(mDate=mDate)
		today = time.strftime('%Y-%m-%d',time.localtime())
		disable = ""
		if mDate < today:
			disable = True
		# 把所有菜品名称返回初始化下拉框
		allFood = Food.objects.values("fName")
		fList = []
		for n in allFood:
			fList.append(n)
		return render(request,"edit_menu.html",{"thisMenu":thisMenu,"allFood":json.dumps(fList),"disable":disable})


@login_required
def edit_menu_check(request):
	if request.POST:
		mDate = request.POST['mDate']
		bre   = request.POST['bre']
		lun   = request.POST['lun']
		din   = request.POST['din']
		thisMenu = Menu.objects.filter(mDate=mDate).update(bre=bre,lun=lun,din=din)
		return HttpResponseRedirect("/")
