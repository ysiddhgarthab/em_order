from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import calendar
import time
import datetime
from OrderModel.models import Order


#返回一个包含本月所有日期以及这些日期对应星期几的列表
def getCurWeek():
	week_day_dict = {
		0 : '星期一',
		1 : '星期二',
		2 : '星期三',
		3 : '星期四',
		4 : '星期五',
		5 : '星期六',
		6 : '星期天',
  	}
	dateList = []
	i = 1
	days  = calendar.monthrange(int(time.strftime('%Y',time.localtime())),int(time.strftime('%m',time.localtime())))[1]
	while i <= days:
		oneDay = []
		d = str(i)
		if i < 10:
			d = '0'+str(i)
		sDate = time.strftime('%Y-%m-'+d,time.localtime())
		week_day = week_day_dict[datetime.datetime.strptime(sDate,'%Y-%m-%d').weekday()]
		oneDay.append(sDate)
		oneDay.append(week_day)
		dateList.append(oneDay)
		i += 1
	return dateList


@login_required
def order(request):
	dateList  = getCurWeek()
	startDate = dateList[0][0]
	stopDate  = dateList[-1][0]
	order = Order.objects.filter(oDate__range=(startDate,stopDate),eId=request.session['eId'])
	#判断用户本月是否已经报餐，如果已报餐就把报餐数据格式化后返回前台显示，否则返回一个时间列表
	if order:
		for index,item in enumerate(order):
			dateList[index].append(item.bre)
			dateList[index].append(item.lun)
			dateList[index].append(item.din)
		print(dateList)
		return render(request,'order.html',{"order":dateList})
	return render(request,'order.html',{"dateList":dateList})


@login_required
def order_check(request):
	dateList = getCurWeek()
	ifOrder = Order.objects.filter(oDate=dateList[0][0],eId=request.session['eId'])
	#判断用户本月是否已经报餐，如果已经报餐执行更新操作，否则执行添加操作
	#更新
	if ifOrder:
		for i in dateList:
			bre = request.POST.get(i[0]+'bre',0)
			lun = request.POST.get(i[0]+'lun',0)
			din = request.POST.get(i[0]+'din',0)
			order = Order.objects.filter(oDate=i[0],eId=request.session['eId']).update(bre=bre,lun=lun,din=din)
		return HttpResponseRedirect("/order")
	#添加
	else:
		for i in dateList:
			bre = request.POST.get(i[0]+'bre',0)
			lun = request.POST.get(i[0]+'lun',0)
			din = request.POST.get(i[0]+'din',0)
			order = Order(eId=request.session['eId'],oDate=i[0],bre=bre,lun=lun,din=din)
			order.save()
		return HttpResponseRedirect("/order")