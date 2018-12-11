from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import calendar
import time
import datetime
from OrderModel.models import Order


#返回一个所传参数月份中所有日期以及这些日期对应星期几的列表
def getCurWeek(year,month):
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
	days  = calendar.monthrange(year,month)[1]
	if month<10:
		month = '0'+str(month)
	while i <= days:
		oneDay = []
		d = str(i)
		if i < 10:
			d = '0'+d
		sDate = str(year)+'-'+str(month)+'-'+d
		#把字符串类型的日期转换为时间日期以便获取日期对应星期几
		strfSdate = datetime.datetime.strptime(sDate, '%Y-%m-%d')
		week_day = week_day_dict[strfSdate.weekday()]
		oneDay.append(sDate)
		oneDay.append(week_day)
		dateList.append(oneDay)
		i += 1
	return dateList


@login_required
def order(request):
	#获得当前年月以及本月里面所有的日期
	lastMonth = []
	nextMonth = []
	now = datetime.datetime.now()	
	year = now.year
	month = now.month
	selectMonth = [year,month]
	dateList  = getCurWeek(year,month)
	#判断是否有GET提交的参数，如果有则将年月设置成为提交的年月
	if request.GET:
		year = int(request.GET['year'])
		month = int(request.GET['month'])
		selectMonth = [year,month]
		dateList = getCurWeek(year,month)
	#月份等于12的处理	
	if month == 12:
		nextMonth.append(year+1)
		nextMonth.append(1)
	else:
		nextMonth.append(year)
		nextMonth.append(month+1)
	#月份等于1的处理
	if month == 1:
		lastMonth.append(year-1)
		lastMonth.append(12)
	else:
		lastMonth.append(year)
		lastMonth.append(month-1)
	#从月份列表中取出开始日期和结束日期到数据库中查询数据
	startDate = dateList[0][0]
	stopDate  = dateList[-1][0]
	order = Order.objects.filter(oDate__range=(startDate,stopDate),eId=request.session['eId'])
	#如果现在是下午5点之后，则不能修改明天的订餐
	curTime = int(time.strftime("%H%M%S"))
	limit = ""
	if curTime>170000:
		limit = datetime.date.today() + datetime.timedelta(days=1)
	else:
		limit = datetime.date.today()
	#根据查询结果判断用户是否报餐，如果已报餐就把报餐数据格式化后返回前台显示，否则返回一个时间列表
	if order:
		for index,item in enumerate(order):
			dateList[index].append(item.bre)
			dateList[index].append(item.lun)
			dateList[index].append(item.din)
			if item.oDate <= limit:
				dateList[index].append(True)
			else:
				dateList[index].append(False)
		return render(request,'order.html',{"order":dateList,"lastMonth":lastMonth,"nextMonth":nextMonth,"selectMonth":selectMonth})
	else:
		limit = datetime.datetime.strptime(str(limit), '%Y-%m-%d')
		for index,item in enumerate(dateList):
			if datetime.datetime.strptime(item[0], '%Y-%m-%d') <= limit:
				dateList[index].append(True)
			else:
				dateList[index].append(False)
		return render(request,'order.html',{"firstOrder":dateList,"lastMonth":lastMonth,"nextMonth":nextMonth,"selectMonth":selectMonth})


@login_required
def order_check(request):
	if request.POST:
		year = int(request.POST['selectYear'])
		month = int(request.POST['selectMonth'])
		next = request.POST['next']
		dateList = getCurWeek(year,month)
		ifOrder = Order.objects.filter(oDate=dateList[0][0],eId=request.session['eId'])
		#判断用户本月是否已经报餐，如果已经报餐执行更新操作，否则执行添加操作
		#更新
		if ifOrder:
			for i in dateList:
				bre = request.POST.get(i[0]+'bre',0)
				lun = request.POST.get(i[0]+'lun',0)
				din = request.POST.get(i[0]+'din',0)
				order = Order.objects.filter(oDate=i[0],eId=request.session['eId']).update(bre=bre,lun=lun,din=din)
			return HttpResponseRedirect(next)
		#添加
		else:
			for i in dateList:
				bre = request.POST.get(i[0]+'bre',0)
				lun = request.POST.get(i[0]+'lun',0)
				din = request.POST.get(i[0]+'din',0)
				order = Order(eId=request.session['eId'],oDate=i[0],bre=bre,lun=lun,din=din)
				order.save()
			return HttpResponseRedirect(next)