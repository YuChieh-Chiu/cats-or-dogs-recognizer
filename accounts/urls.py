from django.urls import path
from . import views # 引用這個資料夾中的views檔案

urlpatterns = [
    path('', views.log_in, name='login'),
    path('logout', views.log_out, name='logout')
]