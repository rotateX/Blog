from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.conf import settings
from apps.blog.models import Article, Category, Tag

# Create your views here.
months = Article.objects.datetimes('pub_time', 'month', order='DESC')
categories = Category.objects.all()
tags = Tag.objects.all()

def base(request):
    return render(request, 'base.html')

def home(request): # 主页
    article_objs = Article.objects.filter(status='p')
    article_pages = Paginator(article_objs, settings.PAGE_NUM)
    page = request.GET.get('page')

    try:
        article_objs_list = article_pages.page(page)
    except PageNotAnInteger:
        article_objs_list = article_pages.page(1)
    except EmptyPage:
        article_objs_list = article_pages.page(article_pages.num_pages)
    return render(request, 'home.html', {
        'article_objs_list':article_objs_list,
        'article_pages':article_pages,
        'category_list':categories,
        'months':months,
    })

def detail(request, id): # 文章详情
    try:

        post = Article.objects.get(id=str(id))
        post.up_view()  # 更新浏览次数
        tags = post.tag.all()  # 获取文章对应所有标签
        next_article = post.next_article()
        pre_article = post.pre_article()

    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {
        'post': post,
        'tags': tags,
        'next_article':next_article,
        'pre_article':pre_article,
    })

# 按时间归档文章
def archives(request, year, month):
    article_objs = Article.objects.filter(pub_time__year=year, pub_time__month=month, status='p').order_by('-pub_time')
    paginator = Paginator(article_objs, settings.PAGE_NUM)
    try:
        page = request.GET.get('page')
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return render(request, 'archives.html', {
        'article_list':article_list,
        'category_list':categories,
        'months':months,
        'year_month':year+'年'+month+'月'

    })

def category(request, id): # 分类归档
    article_objs = Article.objects.filter(category_id=str(id), status='p')
    category = categories.get(id=str(id))
    paginator = Paginator(article_objs, settings.PAGE_NUM)
    try:
        page = request.GET.get('page')
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {
        'article_list':article_list,
        'category':category,
        'category_list':categories,
        'months':months,
        'paginator':paginator,
    })





