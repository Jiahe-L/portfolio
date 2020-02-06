from django.contrib import admin
from .models import Gallery
#上一行为新添加
# Register your models here.


admin.site.register(Gallery)
#注册“Gallery”model，之后用cmd中help迁移数据库，makemigrations和migrate
#迁移后可进入../admin页面查看，添加model(要访问界面，创建createsuperuser)
#之后去views.py导入 model类型文件‘gallery中的models（py文件）’