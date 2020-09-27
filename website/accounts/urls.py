from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [


    ### ACCESSO

    path('registerForm/', views.registerForm, name="registerForm"),
    path('loginForm/',views.loginForm, name="loginForm"),
    path('logout/', views.logoutUser, name = "logout"),

    path('changePassword/', auth_views.PasswordResetView.as_view(), name = "reset_password"),
    path('changePassword_sent/', auth_views.PasswordResetDoneView.as_view(), name ="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    # uidb64= id utente in base 64, token x controllare se è valida
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    ### PARTE ADMIN


    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('customer/<str:pk>/', views.customer, name = "customer"),
    path('products/', views.products, name = "products"),


    ### PARTE UTENTE


    path('', views.home , name="home"),
    path('user', views.userPage, name="user"),
    #path('shop', views.shop, name="shop"),
    path('account/', views.accountSettings, name = "account"),







]