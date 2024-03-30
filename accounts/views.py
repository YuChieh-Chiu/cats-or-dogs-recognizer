from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# 登入
def log_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/homepage')  # 導向首頁
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 登出
def log_out(request):
    logout(request)
    return redirect('/') # 重新導向到登入畫面