from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=16, unique=True, verbose_name='用户名', blank=False)
    password = models.CharField(max_length=128, verbose_name='密码', blank=False)
    email = models.EmailField(max_length=254, unique=True, verbose_name='邮箱')
    createtime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='是否激活',)
    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-createtime']
        verbose_name = '用户'
        verbose_name_plural = '用户组'
