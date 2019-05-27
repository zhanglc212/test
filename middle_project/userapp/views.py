import hashlib
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.shortcuts import render, redirect,HttpResponse


# Create your views here.
from mainapp.models import TUser,TConfirmString
from middle_project import settings


def regist(request):
    return render(request,'register.html')


def hash_code(name, now):
    h=hashlib.md5()
    name+=now
    h.update(name.encode())
    return h.hexdigest()


def make_confirm_string(new_user):
    now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ucode=hash_code(new_user.username,now)
    TConfirmString.objects.create(ucode=ucode,user=new_user)
    return ucode


def send_email(email,ucode):
    subject= 'hello'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/userapp/confirm/?ucode={}"target = blank > 点击，验证邮箱 </a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</ p>'.format('127.0.0.1:8000',ucode)
    msg = EmailMultiAlternatives(subject, text_content,settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html"),
    msg.send()



def saveregist(request):
    try:
        with transaction.atomic():
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")
            code = request.session.get("code")
            captcha = request.POST.get("captcha")
            t = TUser.objects.filter(username=username).count()
            # print(code,captcha,password2,password)
            if not t:
                if code == captcha and password == password2:
                    new_user=TUser.objects.create(email=email, username=username, password=password)
                    #创建邮箱验证码
                    ucode = make_confirm_string(new_user)
                    print('haha','0')
                    send_email(email,ucode)
                    return HttpResponse('前往邮箱验证。。。')
            return redirect("regist")
    except:
        return redirect("regist")

def confirm(request):
    ucode=request.GET.get('ucode')
    confirm1=TConfirmString.objects.filter(ucode=ucode)[0]
    if confirm1:
        user=TUser.objects.filter(id=confirm1.user_id)[0]
        user.status='1'
        user.save()
        username=user.username
        email=user.email
        request.session["flag"] = '1'
        request.session["login"] = "OK"
        request.session["username"] = username
        request.session["email"] = email
        flag_from = request.session.get('flag_from')
        if flag_from == 'car':
            return redirect('indent')
        return redirect('regist_ok')
    else:
        return HttpResponse('regist')

def regist_ok(request):
    email=request.session.get('email')
    return render(request,'register ok.html',{
        'email':email
    })
