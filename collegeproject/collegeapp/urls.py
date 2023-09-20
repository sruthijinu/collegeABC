from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form',views.form,name='form'),
    path('formfill',views.formfill,name='formfill'),
    path('detail1',views.detail1,name='detail1'),
    path('detail2',views.detail2,name='detail2'),
    path('detail3',views.detail3,name='detail3'),
    path('detail4',views.detail4,name='detail4'),
    path('detail5',views.detail5,name='detail5'),

]