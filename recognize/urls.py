from django.urls import path
from . import views # 引用這個資料夾中的views檔案

urlpatterns = [
    path("", views.recognizer, name="recognize"),
    path("result", views.ajax_model_predict, name="predict_result")
]
