from django.db import models
from django.utils import timezone

# 只要 models.py 檔案有任何變動，都要在 terminal 執行一次以下程式碼
# python manage.py makemigrations
# python manage.py migrate

class RecognizerLog(models.Model):
    image = models.ImageField(upload_to="images/", 
                            blank=False, 
                            null=False) # blank, null = False 必填
    upload_time = models.DateField(default=timezone.now)
    prediction = models.CharField(max_length=255, default="Null") # 預測結果
    real = models.CharField(max_length=255, default="Null") # 實際結果
    correct = models.IntegerField(blank=True, default=0) # 預測結果與實際結果相同嗎？相同為1，不同為0