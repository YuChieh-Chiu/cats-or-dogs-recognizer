from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# 首頁，純前端頁面，無後端資料交換
@login_required(login_url="login")
def homepage(request):
    return render(request, 'homepage/homepage.html')