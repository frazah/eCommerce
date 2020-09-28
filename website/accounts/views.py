from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from .models import *
from .forms import *
from .filters import OrderFilter
from .decorators import *

# Create your views here.

def registerForm(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Utente '+ username +' creato')

            return redirect('loginForm')
    tabella= {'form':form}
    return render(request, 'accounts/register.html', tabella)


@unauthenticated_user
def loginForm(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  #prendo i valori da questi campi, nell'html vengono dai 2 input

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username o password errati')



    tabella= {}
    return render(request, 'accounts/login.html', tabella)


def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['admin'])
def home(request):
    orders = Order.objects.all()
    users = Customer.objects.all()


    tot_customers = users.count()
    tot_orders = orders.count()

    delivered = orders.filter(status='Consegnato').count()
    sent = orders.filter(status='Spedito').count()
    pending = orders.filter(status='In elaborazione').count()

    tabella = {'orders':orders , 'users':users , 'tot_orders':tot_orders ,
               'delivered':delivered, 'sent':sent, 'pending':pending}

    return render(request, 'accounts/dashboard.html', tabella)


#@login_required(login_url='loginForm')
#@allowed_users(allowed_roles = ['customer','admin'])
def shop(request):
    products = Product.objects.all()
    tabella = {'products':products}
    return render(request, 'accounts/shop.html', tabella)

def cart(request):
    products = Product.objects.all()
    tabella = {}
    return render(request, 'accounts/cart.html', tabella)

def checkout(request):
    products = Product.objects.all()
    tabella = {}
    return render(request, 'accounts/checkout.html', tabella)









@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['admin'])
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['admin'])
def customer(request,pk):
    user = Customer.objects.get(id = pk)

    orders = user.order_set.all()
    orders_tot =orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    tabella = {'user':user ,'orders':orders, 'orders_tot':orders_tot, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html',tabella)

@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['admin'])
def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer, Order, fields=('product', 'status'), extra = 6)
    user= Customer.objects.get(id=pk)
    formset= OrderFormSet(queryset=Order.objects.none() ,instance=user)
    #form = OrderForm(initial={'user':user})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=user)

        if formset.is_valid():
            formset.save()
            return redirect('/')


    tabella = {'formset':formset}
    return render(request, 'accounts/orderForm.html', tabella)

@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['admin'])
def updateOrder(request,pk):


    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('/')

    tabella = {'form':form}
    return render(request, 'accounts/orderForm.html', tabella)

@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    tabella = {'order':order}
    return render(request, 'accounts/delete.html', tabella)


@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['customer'])
def accountSettings(request):
    customer  = request.user.customer
    form = CustomerForm(instance = customer)


    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance = customer)
        if form.is_valid():
            form.save()

    tabella = {'form':form}
    return render(request, 'accounts/account_settings.html', tabella)





@login_required(login_url='loginForm')
@allowed_users(allowed_roles = ['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    tot_orders = orders.count()

    delivered = orders.filter(status='Consegnato').count()
    sent = orders.filter(status='Spedito').count()
    pending = orders.filter(status='In elaborazione').count()

    tabella = {'orders':orders, 'tot_orders':tot_orders, 'delivered': delivered, 'sent':sent, 'pending':pending}
    return render(request, 'accounts/user.html',tabella)