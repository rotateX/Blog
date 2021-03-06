"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from apps.blog import views as blog_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from apps.login import views as login_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', blog_views.home, name='home'),
    path('articles/<int:id>/', blog_views.detail, name='post'),
    path('archives/<str:year>/<str:month>', blog_views.archives, name='archives'),
    path('category/<str:id>', blog_views.category, name='category'),
    url(r'mdeditor/', include('mdeditor.urls')),
    path('favicon.ico', serve, {'path': 'static/image/favicon.ico'}), # 处理找不到favicon.ico 问题
    path('login/', login_views.signin, name='login') ,
    path('register/', login_views.signup, name='register'),
    path('register/successful/', login_views.regs_scf, name='regs_scf'),
    path(r'activate/', login_views.activate,name='activate'),
]
# 处理DEBUG = False 下找不到静态资源
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]


