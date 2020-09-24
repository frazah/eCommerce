from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *

# Create your views here.

def home(request):
    orders = Order.objects.all()
    users = User.objects.all()


    tot_customers = users.count()
    tot_orders = orders.count()

    delivered = orders.filter(status='Consegnato').count()
    sent = orders.filter(status='Spedito').count()
    pending = orders.filter(status='In elaborazione').count()

    tabella = {'orders':orders , 'users':users , 'tot_orders':tot_orders ,
               'delivered':delivered, 'sent':sent, 'pending':pending}

    return render(request, 'accounts/dashboard.html', tabella)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})

def customer(request,pk):
    user = User.objects.get(id = pk)

    orders = user.order_set.all()
    orders_tot =orders.count()

    tabella = {'user':user ,'orders':orders, 'orders_tot':orders_tot}
    return render(request, 'accounts/customer.html',tabella)

def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(User,Order, fields=('product','status'), extra = 6)
    user= User.objects.get(id=pk)
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


def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    tabella = {'order':order}
    return render(request, 'accounts/delete.html', tabella)