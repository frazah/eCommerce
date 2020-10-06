from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django.contrib import admin
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.conf.urls import url,include
from django_otp.views import LoginView
class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)


admin.site.__class__ = OTPAdminSite





urlpatterns = [


    ### ACCESSO

   #url(r'^admin/',admin_site.urls),
   #url(r'^dadmin/',admin.site.urls),
    url(r'^adminhoney/',include('admin_honeypot.urls',namespace='admin_honeypot')),
    path('registerForm/', views.registerForm, name="registerForm"),
    path('loginForm/',views.loginForm, name="loginForm"),
    path('logout/', views.logoutUser, name = "logout"),

    path('changePassword/', auth_views.PasswordResetView.as_view(template_name="accounts/changePassword.html"), name = "reset_password"),
    path('changePassword_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/passwordResetSent.html"), name ="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/passwordResetForm.html"),
         name = "password_reset_confirm"),
    # uidb64= id utente in base 64, token x controllare se è valida
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/passwordResetComplete.html"),
         name="password_reset_complete"),

    ### PARTE ADMIN


    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('customer/<str:pk>/', views.customer, name = "customer"),
    path('products/', views.products, name = "products"),


    ### PARTE UTENTE


    path('', views.shop , name="home"),
    path('user', views.userPage, name="user"),
    path('dashboard', views.home, name="dashboard"),
    path('account/', views.accountSettings, name = "account"),
    path('cart/', views.cart,name= "cart"),
    path('checkout', views.checkout, name = "checkout"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('process_order/', views.processOrder, name = "process_order"),








]