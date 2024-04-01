
from django.urls import path

from acc3 import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('register/login.html', views.login_view, name='login_html'),
    path('user/', views.user, name='user'),
    path('dealer/', views.dealer, name='dealer'),
]