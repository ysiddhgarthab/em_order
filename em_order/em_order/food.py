# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse,HttpResponseRedirect
from OrderModel.models import Food
from django.conf import settings
import time
from django.shortcuts import render_to_response
import json
from django.contrib.auth.decorators import login_required


@login_required
def add_food(request):
    return render(request,'add_food.html')


# 接收POST请求数据
@login_required
def add_food_check(request):
    if request.POST:
        fName  = request.POST['fName']
        fType  = request.POST['fType']
        fSpicy = request.POST['fSpicy']
        fCost  = request.POST['fCost']
        fDesc  = request.POST['fDesc']

        # 获取用户提交的图片并根据图片名设置路径
        pic     = request.FILES.get('fPic')
        timestr = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())));
        fPic    = "OrderModel/"+timestr+pic.name

        # 把用户提交的数据和图片的路径存入到数据库中去
        fo   = Food(fName=fName,fType=fType,fSpicy=fSpicy,fCost=fCost,fDesc=fDesc,fPic=fPic)
        fo.save()

        #把用户上传的图片写入到设置的路径中
        filePath = settings.MEDIA_ROOT+"/"+fPic
        with open(filePath,'wb') as p:
        	for b in pic.chunks():
        		p.write(b)

    return HttpResponseRedirect("/add_food")
