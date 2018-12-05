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
    mod_food(request)
    return HttpResponseRedirect("/add_food")



def food_admin(request):
    if request.POST:
        keyWord = request.POST.get('keyWord','')
        fType = request.POST['fType']
        AllFood=Food.objects.filter(fName__icontains=keyWord)
        if fType:
            AllFood=Food.objects.filter(fName__icontains=keyWord,fType=fType)
        return render(request,"food_admin.html",{"AllFood":AllFood})
    AllFood = Food.objects.all()
    return render(request,"food_admin.html",{"AllFood":AllFood})



def edit_food(request):
    if request.GET:
        fId = request.GET['fId']
        thisFood = Food.objects.filter(id=fId)
        return render(request,"edit_food.html",{"thisFood":thisFood[0]})
    if request.POST:
        mod_food(request)
        return HttpResponseRedirect("/food_admin")


def mod_food(request):
    if request.POST:
        fId    = request.POST.get('fId','')
        fName  = request.POST['fName']
        fType  = request.POST['fType']
        fSpicy = request.POST['fSpicy']
        fCost  = request.POST['fCost']
        fDesc  = request.POST['fDesc']

        if fCost.strip() == "":
            fCost = 0
        
        food = ""
        #根据有没有接受到菜品id判断是新增还是更新操作，如果是更新操作，再看用户有没有上传图片，如果有上传图片
        #则用新上传的图片来代替本来的(不改变图片名,只覆盖内容)，如果是新增操作，用户有上传图片则把图片名存进数据库
        #否则存入一个空字符串
        if fId:
            food = Food.objects.filter(id=fId)

        # 获取用户提交的图片并根据图片名设置路径
        fPic =""
        pic = request.FILES.get('fPic')
        if pic:
            if food:
                fPic = str(food[0].fPic)
            else:
                timestr = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())));
                fPic    = "OrderModel/"+timestr+pic.name
            #把用户上传的图片写入到设置的路径中
            filePath = settings.MEDIA_ROOT+"/"+fPic
            with open(filePath,'wb') as p:
                for b in pic.chunks():
                    p.write(b)

        #执行新增或更新操作
        if food:
            food.update(fName=fName,fType=fType,fSpicy=fSpicy,fCost=fCost,fDesc=fDesc)
            
        else:
            fo   = Food(fName=fName,fType=fType,fSpicy=fSpicy,fCost=fCost,fDesc=fDesc,fPic=fPic)
            fo.save()
            