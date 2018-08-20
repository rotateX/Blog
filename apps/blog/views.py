from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.conf import settings
from apps.blog.models import Article

# Create your views here.
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
    return render(request, 'home.html', {'article_objs_list': article_objs_list})

def detail(request, id):
    try:

        post = Article.objects.get(id=str(id))
        post.up_view()  # 更新浏览次数
        tags = post.tag.all()  # 获取文章对应所有标签
        next_aticle = post.next_aticle()
        pre_aticle = post.pre_aticle()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'tags': tags, 'next_aticle':next_aticle, 'pre_aticle':pre_aticle})




