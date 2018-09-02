from django.db import models
from django.contrib.auth.hashers import make_password
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired
from itsdangerous import BadSignature,SignatureExpired
from django.conf import settings

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
    # 添加用户时密码加密保存

    def save(self, *args, **kwargs):
        if not self.password.startswith('md5'):
            self.password = make_password(self.password)
        super().save()
    # 生成token
    def generate_activate_token(self, expires_in=3600):
        s = Serializer(settings.SECRET_KEY, expires_in)
        return s.dumps({'id': self.id})

    # token校验
    @staticmethod
    def check_activate_token(token):
        s = Serializer(settings.SECRET_KEY)
        try:
            data = s.loads(token)
        except BadSignature:
            return '无效的激活码'
        except SignatureExpired:
            return '激活码已过期'
        user = UserInfo.objects.filter(id=data.get('id'))[0]
        if not user:
            return '激活的账号不存在'
        if not user.is_active:
            user.is_active = True
            user.save()
        return '激活成功'