import numpy as np
from django.shortcuts import render, redirect
from .models import RecognizerLog
from .forms import UploadImageForm
from .convnet import convnets, preprocess_test_data
from django.contrib.auth.decorators import login_required

# 將上傳圖片的表單傳送至Django Template(樣板)來進行顯示
@login_required(login_url="login")
def recognizer(request):
    """
    一些資料庫抽象API語法跟SQL語法的對照
    (1)
    posts = Post.objects.all()
    #SELECT * FROM posts_post
    (2)
    posts = Post.objects.filter(location="台南")
    # SELECT * FROM posts_post WHERE location="台南"
    (3)
    posts = Post.objects.get(id=1)
    # SELECT * FROM posts_post WHERE id=1
    ----------
    回傳Django Template的語法
    render(
        request,
        template_name, # 樣板名稱 
        context # 要帶入樣板的資料，以dict型態傳輸
        )

    """
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
            # 模型判讀區塊
            photo = RecognizerLog.objects.last()
            train_x = train_y = valid_x = valid_y = np.zeros((2, 2))
            cats_and_dogs_recognizer = convnets(train_x, train_y, valid_x, valid_y)
            print("INITIALIZE CONVNETS - DONE.")
            test_x = preprocess_test_data(photo.image.url)
            print("PREPROCESS TEST DATA - DONE.")
            if test_x is None:
                model_pred = "no prediction."
            else:
                model_pred = cats_and_dogs_recognizer.predict(test_x)
                print("PREDICT - DONE.")
            request.session["pred"] = model_pred # 模型預測的結果，存進 session 中，方便後面取用
            print(request.session["pred"])
            context = {
                "pred": request.session["pred"],
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
