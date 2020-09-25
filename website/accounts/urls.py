from django.urls import path
from . import views

urlpatterns = [

    path('registerForm/', views.registerForm, name="registerForm"),
    path('loginForm/',views.loginForm, name="loginForm"),
    path('logout/', views.logoutUser, name = "logout"),

    path('', views.home , name="home"),
    path('products/', views.products, name = "products"),
    path('customer/<str:pk>/', views.customer, name = "customer"),
    path('profile', views.profile, name="profile"),
    #path('shop', views.shop, name="shop"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]