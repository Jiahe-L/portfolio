from django.db import models

# Create your models here.
# Model修改之后，要去命令行迁移数据库


class Gallery(models.Model):
	description = models.CharField(default='在此输入作品简介', max_length=100)
	image = models.ImageField(default='default.png', upload_to='images/')
	title = models.CharField(default='作品标题', max_length=50)#方便管理

	def __str__(self):
		return self.title
