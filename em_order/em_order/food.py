# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse,HttpResponseRedirect
from OrderModel.models import Food,Score
from django.conf import settings
import time
from django.shortcuts import render_to_response
import json
from django.contrib.auth.decorators import login_required
import os


@login_required
def add_food(request):
    return render(request,'add_food.html')


# 接收POST请求数据
@login_required
def add_food_check(request):
    mod_food(request)
    return HttpResponseRedirect("/add_food")


@login_required
def food_admin(request):
    if request.POST:
        keyWord = request.POST.get('keyWord','')
        fType = request.POST['fType']
        AllFood=Food.objects.filter(fName__icontains=keyWord)
        if fType:
            AllFood=Food.objects.filter(fName__icontains=keyWord,fType=fType)
        return render(request,"food_admin.html",{"AllFood":AllFood})
    AllFood = Food.objects.all()
    message = request.GET.get('message','')
    return render(request,"food_admin.html",{"AllFood":AllFood,"message":message})


@login_required
def edit_food(request):
    if request.GET:
        fId = request.GET['fId']
        thisFood = Food.objects.filter(id=fId)
        return render(request,"edit_food.html",{"thisFood":thisFood[0]})
    if request.POST:
        mod_food(request)
        return HttpResponseRedirect("/food_admin?message=保存成功！")


@login_required
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
        fPic =""
        #判断用户有没有上传图片
        pic = request.FILES.get('fPic')
        #判断是更新还是新增操作
        if fId:
            food = Food.objects.filter(id=fId)
        # 用户有上传图片才执行以下操作
        if pic:
            #如果之前有上传过图片
            if food and food[0].fPic != '':
                fPic = str(food[0].fPic)
            #如果之前没有上传过图片
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
            food.update(fName=fName,fType=fType,fSpicy=fSpicy,fCost=fCost,fDesc=fDesc,fPic=fPic)
            
        else:
            fo   = Food(fName=fName,fType=fType,fSpicy=fSpicy,fCost=fCost,fDesc=fDesc,fPic=fPic)
            fo.save()


@login_required
def del_food(request):
    if request.GET:
        fId = request.GET['fId']
        food = Food.objects.filter(id=fId)
        if food[0].fPic:
            picPath = settings.MEDIA_ROOT+"/"+str(food[0].fPic)
            if(os.path.exists(picPath)):
                os.remove(picPath)
        food.delete()
    return HttpResponseRedirect("/food_admin?message=删除成功！")


def food_detail(request):
    if request.GET:
        fName = request.GET['fName']
        mDate = request.GET.get('mDate','')
        food = Food.objects.filter(fName=fName)
        today = time.strftime('%Y-%m-%d',time.localtime())
        disable = False
        if mDate != today:
            disable = True
    return render(request,"food_detail.html",{"food":food[0],"disable":disable})

@login_required
def score(request):
    if request.POST:
        fName = request.POST['fName']
        score = request.POST['score']
        comment = request.POST['comment']
        sDate = time.strftime('%Y-%m-%d',time.localtime())
        user_id = request.session['id']

        s = Score.objects.filter(fName=fName,sDate=sDate,user_id=user_id)
        if s:
            return HttpResponseRedirect("/?message=你已评价过此菜品！")
        score = Score(fName=fName,score=score,comment=comment,sDate=sDate,user_id=user_id)
        score.save()
        return HttpResponseRedirect("/?message=发表评价成功！")
    return HttpResponseRedirect("/")
