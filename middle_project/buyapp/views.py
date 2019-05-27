import random,string
from datetime import date, datetime

from django.db import transaction
from django.http import JsonResponse, response
from buyapp.cart import Cart
from django.shortcuts import render, HttpResponse, redirect
from mainapp.models import TBook, TUser,TAddress,TOrder,TOrderitem

# 购物车页面
def car(request):
    flag = request.session.get('flag')
    uname = request.session.get('username')
    cart = request.session.get('cart')
    if cart:
        goods_info = cart.cartitem
        all_num = 0
        for i in goods_info:
            all_num += i.amount
        # print(amount)
        return render(request,'car.html',{
            'goods_info':goods_info,
            'cart':cart,
            'all_num':all_num,
            'flag':flag,
            'uname':uname,

        })
    else:
        print('22')
        all_num=0
        return render(request,'car.html',{
            'all_num':all_num
        })

# 添加至购物车
def add(request):
        bookid = request.GET.get('bookid')
        num = request.GET.get('num')
        cart = request.session.get('cart')
        if cart is None:
            cart = Cart()
            cart.add_book(bookid,num)
            request.session['cart'] = cart
        else:
            cart.add_book(bookid,num)
            request.session['cart'] = cart
        return JsonResponse({'fail':'添加成功'},safe=False)


# 删除购物车中的图书
def del_book_info(request):
    bookid = request.GET.get('bookid')
    cart = request.session.get('cart')
    cart.delete_cart(bookid)
    request.session['cart'] = cart
    return redirect('car')

# 修改购物车中书籍数量
def change_goodsNum(request):
    cart = request.session.get('cart')
    bookid = request.GET.get('bookid')
    amount = request.GET.get('amount')
    cart.modify_cart(bookid,amount)
    request.session['cart'] = cart
    cart=request.session.get('cart')
    total_price=cart.total_price
    save_price=cart.save_price
    all_num=0
    for i in cart.cartitem:
        all_num += i.amount
    print(all_num)

    return JsonResponse({
        'total_price': total_price,
        'save_price':save_price,
        'all_num': all_num
        },safe=False)
# 地址,订单信息
def indent(request):
    flag = request.session.get('flag')
    flag_from=request.GET.get('flag_from')
    request.session['flag_from']=flag_from
    uname = request.session.get('username')
    if flag=='1':  #如果是登录状态
        uname_id = TUser.objects.filter(username=uname)[0].id
        addresses=TAddress.objects.filter(user_id=uname_id)
        cart = request.session.get('cart')  #获取购物车信息
        cartitem=cart.cartitem
        return render(request,'indent.html',{
            'uname':uname,
            'addresses':addresses,
            'cart':cart,
            'cartitem':cartitem
            })
    else:
        return redirect('login')

#显示地址
def old_address(request):
    address_id = request.GET.get('address_id')
    address = TAddress.objects.filter(address_id=address_id)[0]
    return JsonResponse({'address_address': address.address,
                         'address_name': address.name,
                         'address_potal': address.potal,
                         'address_phone': address.phone,
                         'address_mobile': address.mobile
                         }, safe=False)

# 订单成功页
def indent_ok(request):
    flag = request.session.get('flag')
    uname = request.session.get('username')
    if flag=='1':
        address_id = request.POST.get('myselect')
        uname_id = TUser.objects.get(username=uname).id
        if address_id != '0':
            print(address_id, type(address_id))
            address_name=TAddress.objects.filter(address_id=address_id)[0].name
        else:
            address_name = request.POST.get('address_name')
            address_address = request.POST.get('address_address')
            address_potal = request.POST.get('address_potal')
            address_phone = request.POST.get('address_phone')
            address_mobile = request.POST.get('address_mobile')
            TAddress.objects.create(name=address_name, address=address_address, potal=address_potal,
                                    phone=address_phone,mobile=address_mobile,user_id=uname_id)
            address_id=TAddress.objects.filter(name=address_name)[0].address_id  #新建地址ID
        order_num=random.randint(1000000,9999999999)
        TOrder.objects.create(order_num=order_num,address_id=address_id,user_id=uname_id)
        cart = request.session.get('cart')  # 获取购物车信息
        cartitem = cart.cartitem
        order_id=TOrder.objects.filter(order_num=order_num)[0].id
        sum=0
        for i in cartitem:
            sub_count=i.amount*i.book.dang_price
            sum+=1
            TOrderitem.objects.create(book_id=i.book.id,order_id=order_id,sub_count=sub_count)
        return render(request,'indent ok.html',{
            'uname':uname,
            'order_num':order_num,
            'sum':sum,
            'cart':cart,
            'address_name':address_name

        })
    else:return redirect('login')
