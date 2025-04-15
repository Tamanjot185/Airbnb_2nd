from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cozy/', views.cozy, name='cozycottage'),
    path('house/', views.house, name='house'),
    path('amazing/', views.amazing, name='amazing'),
    path('beachfront/', views.beachfront, name='beachfront'),

]