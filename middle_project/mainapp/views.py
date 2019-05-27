import time
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from mainapp.models import TCategory,TBook,TUser
import random,string
from mainapp.captcha.image import ImageCaptcha


# Create your views here.
def main(request):
    flag=request.session.get('flag')
    uname=request.session.get('username')
    category=TCategory.objects.all()
    books=TBook.objects.all()
    return render(request,'index.html',{
        'category':category,
        'books':books,
        'flag':flag,
        'uname':uname
    })


def bookDetails(request):
    flag = request.session.get('flag')
    uname = request.session.get('username')
    bookid=request.GET.get("bookid")
    # print(bookid)
    book=TBook.objects.filter(id = bookid)[0]
    cate2=TCategory.objects.filter(id=book.category_id)[0] #书所属的二级类
    cate1=TCategory.objects.filter(id=cate2.parent_id)[0]  #书所属的一级类
    # print(cate1,cate2)
    return render(request,'Book details.html',{
        'book':book,
        'cate1':cate1,
        'cate2':cate2,
        'flag':flag,
        'uname':uname,
    })

def bookList(request):
    flag = request.session.get('flag')
    uname = request.session.get('username')
    cate_id=request.GET.get('cate_id')
    cate_pid=request.GET.get('cate_pid')
    cate1 = TCategory.objects.filter(id=cate_id)
    cate2 = TCategory.objects.filter(parent_id=cate_id)
    cate3 = TCategory.objects.filter(id=cate_pid)
    category=TCategory.objects.all()
    if cate_pid:   #如果点击了二级分类
        books=TBook.objects.filter(category__id=cate_pid)
        cate3 = TCategory.objects.filter(id=cate_pid)[0]
        # print(books)
    else:   #如果点击了一级分类
        books=TBook.objects.filter(category__parent_id=cate_id)

    number = request.GET.get("number")
    if not number:
        number = 1
    pagtor = Paginator(books, per_page=3)
    page = pagtor.page(number)  # 获取某一页的页面对象
    return render(request,'booklist.html',{
        'cate_id':cate_id,
        'cate_pid':cate_pid,
        'cate1':cate1,
        'cate2':cate2,
        'cate3': cate3,
        'category':category,
        'page':page,
        'flag': flag,
        'uname': uname
    })

def login(request):

    return render(request,'login.html')


def savelogin(request):
    flag_from = request.session.get('flag_from')
    username = request.POST.get("username")
    password = request.POST.get("password")
    # print(username, password)
    rem = request.POST.get("remember")
    u = TUser.objects.filter(username=username, password=password)
    # print(u)
    if u:
        status = TUser.objects.filter(username=username)[0].status
        if status=='1':
            request.session["flag"] = '1'
            request.session["login"] = "OK"
            request.session["username"] = username
            if flag_from=='car':
                return redirect('indent')
            return redirect("main")
    return redirect('login')
def loginout(request):
    del request.session['username']
    del request.session['flag']
    flag_from = request.session.get('flag_from')
    if flag_from=='car':
        return redirect('display_car')
    return redirect('main')

def getcaptcha(request):  #生成验证码
    img = ImageCaptcha()
    # rand_code = random.sample(string.ascii_letters + string.digits, 4)
    rand_code=random.sample(string.digits,4)
    rand_code="".join(rand_code)
    request.session["code"]=rand_code
    data=img.generate(rand_code)
    return HttpResponse(data,"image/png")

def checkemail(request): #验证邮箱
    email=request.GET.get('email')
    result=TUser.objects.filter(email=email)
    if result:
        return HttpResponse("false")
    else:
        return HttpResponse("true")

def checkname(request): #验证用户名
    time.sleep(3)
    username=request.GET.get('username')
    result=TUser.objects.filter(username=username)
    if result:
        return HttpResponse("false")
    else:
        return HttpResponse("true")
def checkpwdd(request):     #验证密码
    password=request.GET.get('password')
    password2=request.GET.get('password2')
    if password==password2:
        return HttpResponse("密码一致")
    else:
        return HttpResponse("密码不一致")

def checkcode(request):     #验证验证码
    icode=request.GET.get('icode')
    randcode=request.session.get("code")
    # print(icode,randcode)
    if icode.upper()==randcode.upper():
        return HttpResponse("输入正确")
    else:
        return HttpResponse("输入错误")

