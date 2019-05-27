from django.urls import path
from mainapp import views

# mainapp_name='mainapp'
urlpatterns = [
    path('main/',views.main,name="main"),
    path('bookDetails/',views.bookDetails,name="bookDetails"),
    path('bookList/',views.bookList,name='bookList'),
    path('login/',views.login,name='login'),
    path('loginout/', views.loginout, name='loginout'),
    path('savelogin/',views.savelogin,name='savelogin'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('checkemail/', views.checkemail, name='checkemail'),
    path('checkname/',views.checkname,name='checkname'),
    path('checkpwdd/',views.checkpwdd,name='checkpwdd'),
    path('checkcode/', views.checkcode, name='checkcode'),

]
