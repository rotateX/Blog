from django.contrib import admin
from apps.blog.models import Article, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'pub_time', 'views')
    list_per_page = 10
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)  # 给content字段添加富文本

# admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, PostAdmin)





