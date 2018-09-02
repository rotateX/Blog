from django.shortcuts import render, redirect, HttpResponse
from apps.login.models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from apps.login.signupform import loginform
from apps.login.signupform import signupform
from apps.login.email import send_activate_mail
from django.contrib import messages

# 用户登录
def signin(request):
    if request.method == 'POST':
        login_form = loginform(request.POST)
        # errmsg1 = login_form.username.error_messages
        msg = '请检查填写内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # 现在还少了 对用户是否激活状态的判断
            try:
                user = UserInfo.objects.get(username=username)
                user_psw = user.password
                if check_password(password, user_psw):
                    return redirect('home')
            except:
                errmsg = '用户名或密码不正确'
                return render(request, 'signin/signin.html', {'errmsg': errmsg, 'lg_form': login_form})
        return render(request, 'signin/signin.html', {'msg': msg, 'lg_form': login_form,})
    login_form = loginform
    return render(request, 'signin/signin.html', {'lg_form': login_form})







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
    if request.method == 'POST':
        regs_form = signupform(request.POST)
        err = '请检查填写内容'
        if regs_form.is_valid():
            username = regs_form.cleaned_data['username']
            password = regs_form.cleaned_data['password']
            confirm_p = regs_form.cleaned_data['confirm_p']
            email = regs_form.cleaned_data['email']
            if password != confirm_p:
                psw_err = '两次密码不一致'
                return render(request, 'signup/register.html', {'regs_form': regs_form, 'psw_err':psw_err})
            else:
                if UserInfo.objects.filter(username=username).exists():
                    name_err = '用户名已存在'
                    return render(request, 'signup/register.html', {'regs_form': regs_form, 'name_err':name_err})
                elif UserInfo.objects.filter(email=email).exists():
                    email_err = '邮箱已被注册'
                    return render(request, 'signup/register.html', {'regs_form': regs_form, 'email_err':email_err})
                else:
                    msg = '注册成功！'
                    UserInfo.objects.create(username=username.strip(), password=make_password(password, None,'default'), email=email.strip(), is_active=False)
                    u = UserInfo.objects.get(username=username)
                    token = u.generate_activate_token().decode('utf-8')
                    send_activate_mail(request, u.email, '激活账号', 'email', token=token, username=u.username)
                    messages.add_message(request, messages.INFO, '账号注册成功，请前往邮箱激活账号！')
                    return render(request, 'signup/regs_scf.html', {'user': u})
        else:
            # err = regs_form.errors
            return render(request, 'signup/register.html', {'regs_form': regs_form, 'err':err})

    regs_form = signupform
    return render(request, 'signup/register.html', {'regs_form': regs_form})

def activate(request):
    token = request.GET['token']
    result = UserInfo.check_activate_token(token)
    return HttpResponse(result)

def regs_scf(request):
    return render(request, 'signup/regs_scf.html')

