from django.urls import path
from userapp import views
urlpatterns = [
    path('regist/', views.regist, name='regist'),
    path('saveregist/',views.saveregist,name='saveregist'),
    path('regist_ok/',views.regist_ok,name='regist_ok'),
    path('confirm/', views.confirm, name='confirm'),

]
