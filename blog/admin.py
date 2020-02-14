from django.contrib import admin
from . import models # from .models import Blog ; admin.site.regester(Blog)
# Register your models here.

admin.site.register(models.Blog)