"""
URL configuration for recognizer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # 引用include函式
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recognize/", include("recognize.urls")), # 新增應用程式的網址檔案
    path("homepage/", include("homepage.urls")), # 首頁urls
    path("dashboard/", include("dashboard.urls")), # 儀表板urls
    path("", include("accounts.urls")) # 帳號相關的urls
]

# let us fetch image from db and show in html
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
