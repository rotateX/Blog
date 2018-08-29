from django.contrib import admin
from apps.login.models import *
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'createtime', 'is_active')
    list_per_page = 5
    search_fields = ['username']

admin.site.register(UserInfo, UserInfoAdmin)