from django import forms
from .models import RecognizerLog

# 建立讓使用者上傳圖片的表單:
# -> 表單基於 Model 中的資料建立，屬於 ModelForm 
# -> 藉此能夠快速建置基本的CRUD(Create-Read-Update-Delete)表單應用程式。
class UploadImageForm(forms.ModelForm):
    class Meta: # Meta存放表單的背景資訊
        model = RecognizerLog # 表單背後對應的模型
        fields = ('image', ) # 要顯示哪些欄位
        # 客製化表單的顯示外觀: 套用Bootstrap的表單CSS類別
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
        # 表單欄位的標題顯現（預設是顯示Model中的英文名稱）
        labels = {
            'image': '請上傳您的圖片'
        }