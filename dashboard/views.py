from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recognize.models import RecognizerLog

# 儀表板
@login_required(login_url="login")
def dashboard(request):
    photos = RecognizerLog.objects.all() # 取得所有的紀錄
    # 計算指標數值
    pCAT_rCAT = RecognizerLog.objects.filter(prediction="貓咪", real="貓咪").count()
    pCAT_rDOG = RecognizerLog.objects.filter(prediction="貓咪", real="狗狗").count()
    pDOG_rCAT = RecognizerLog.objects.filter(prediction="狗狗", real="貓咪").count()
    pDOG_rDOG = RecognizerLog.objects.filter(prediction="狗狗", real="狗狗").count()
    try:
        precision_of_dogs = round((pDOG_rDOG / (pDOG_rCAT + pDOG_rDOG))*100, 2) #（r狗/p狗）
    except:
        precision_of_dogs = None
    try:
        recall_of_dogs = round((pDOG_rDOG / (pCAT_rDOG + pDOG_rDOG))*100, 2) #（p狗/r狗）
    except:
        recall_of_dogs = None
    try:
        precision_of_cats = round((pCAT_rCAT / (pCAT_rCAT + pCAT_rDOG))*100, 2) #（r貓/p貓）
    except:
        precision_of_cats = None
    try:
        recall_of_cats = round((pCAT_rCAT / (pCAT_rCAT + pDOG_rCAT))*100, 2) #（p貓/r貓）
    except:
        recall_of_cats = None
    # 回傳 context
    context = {
        "photos": photos,
        "precision_of_dogs": precision_of_dogs,
        "recall_of_dogs": recall_of_dogs,
        "precision_of_cats": precision_of_cats,
        "recall_of_cats": recall_of_cats
    }
    return render(request, 'dashboard/dashboard.html', context)