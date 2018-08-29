from django.shortcuts import render, redirect, HttpResponse
from apps.login.models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from apps.login.signupform import signupform

# Create your views here.
# 用户登录
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('form-username', None) # 确保当数据请求中没有username键时不会抛出异常，而是返回默认值None；
        password = request.POST.get('form-password', None)
        email = request.POST.get('form-username', None)
        print('get'+password)
        print(UserInfo.objects.filter(username=username).values('password'))
        # if UserInfo.objects.filter(Q(username=username) | Q(email=email)):
        # if UserInfo.objects.filter(username=username):

        if password == UserInfo.objects.filter(username=username).values('password'):

            request.session['username'] = username
            request.session['is_login'] = True
            return redirect('home')
        else:
            return render(request, 'signin/signin.html', {
                'msg': '用户名或密码错误'
            })
    else:
        return render(request, 'signin/signin.html')

# 获取session
def index(request):
    u_is_login = request.session.get('is_login', False)
    u_session = request.session.get('username')
    if u_is_login:
        return render(request, 'home.html', {
            'username':u_session
        })
    else:
        return render(request, 'signin/signin.html')



# 用户退出



# 注册用户
def signup(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     email = request.POST('email')
    #     UserInfo.objects.create(username=username.strip(), password=make_password(password), email=email.strip(), is_active=False)
    sform = signupform(request.POST)
    return render(request, 'signup/register.html', {
        'form': sform
    })
