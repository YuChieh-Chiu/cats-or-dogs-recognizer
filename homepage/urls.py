from django.urls import path
from . import views # 引用這個資料夾中的views檔案

# 首頁網址
urlpatterns = [
    path("", views.homepage, name="homepage")
]