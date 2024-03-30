from django.contrib import admin
from .models import RecognizerLog

# Display models
class RecognizerLogAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "upload_time", "prediction", "real", "correct")
    # fields = () # 可以選擇要顯示哪些欄位
    # exclude = () # 可以選擇要排除哪些欄位

# Register your models here.
admin.site.register(RecognizerLog, RecognizerLogAdmin) # 註冊至Administration(管理員後台)