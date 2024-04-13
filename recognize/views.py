import json
import numpy as np
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import RecognizerLog
from .forms import UploadImageForm
from .convnet import convnets, preprocess_test_data

# 將上傳圖片的表單傳送至Django Template(樣板)來進行顯示
@login_required(login_url="login")
def recognizer(request):
    pred = None
    photo = RecognizerLog.objects.last() # 查詢最新一筆資料（讓前臺可以永遠顯示最新一筆）
    form = UploadImageForm()
    if request.method == "POST": # 使用者上傳了圖片 or 確認了結果是否正確
        photo = RecognizerLog.objects.last()
        form = UploadImageForm(request.POST, request.FILES)
        if request.POST.get("correct"): # 前台點擊 correct 按鈕
            pred = request.session["pred"] 
            if pred == "貓咪":
                real = "貓咪"
            else:
                real = "狗狗"
            photo.prediction = pred
            photo.real = real
            photo.correct = 1
            photo.save()
            return redirect("/recognize")
        if request.POST.get("wrong"): # 前台點擊 wrong 按鈕
            pred = request.session["pred"] 
            if pred == "貓咪":
                real = "狗狗"
            else:
                real = "貓咪"
            photo.prediction = pred
            photo.real = real
            photo.correct = 0
            photo.save()
            return redirect("/recognize")
        if form.is_valid(): # 上傳圖片且圖片通過 django 預設 csrf 驗證
            form.save()
            photo = RecognizerLog.objects.last()
            context = {
                "pred": "loading",
                "photo": photo,
                "form": form
            }
            return render(request, "recognize/recognizer.html", context) # 重新傳值。因為上傳檔案後，前台模板內容受到變動了，所以不能用 redirect
    context = {
        "pred": pred,
        "photo": photo,
        "form": form
    }
    return render(request, "recognize/recognizer.html", context)

@login_required(login_url="login")
def ajax_model_predict(request):
    # 模型判讀區塊
    photo = RecognizerLog.objects.last()
    train_x = train_y = valid_x = valid_y = np.zeros((2, 2))
    cats_and_dogs_recognizer = convnets(train_x, train_y, valid_x, valid_y)
    test_x = preprocess_test_data(photo.image.url)
    if test_x is None:
        model_pred = "None"
    else:
        model_pred = cats_and_dogs_recognizer.predict(test_x)
    request.session["pred"] = model_pred # 模型預測的結果，存進 session 中，方便後面取用
    context = {
        "pred": request.session["pred"],
    }
    data = json.dumps(context)
    return HttpResponse(data, content_type="application/json")
