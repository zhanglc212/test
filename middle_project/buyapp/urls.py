from django.urls import path
from buyapp import views
urlpatterns=[
    path('add/',views.add,name='add'),
    path('car/',views.car,name='car'),
    path('change_goodsNum/', views.change_goodsNum, name='change_goodsNum'),
    path('del_book_info/', views.del_book_info, name='del_book_info'),
    path('indent/', views.indent, name='indent'),
    path('indent_ok/', views.indent_ok, name='indent_ok'),
    path('old_address/',views.old_address,name='old_address')

]