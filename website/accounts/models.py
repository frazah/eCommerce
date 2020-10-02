from django.db import models
from django.contrib.auth.models import *

# Create your models here.


#qui scriviamo le tabelle del database

class Customer(models.Model):
    user = models.OneToOneField(User, null = True,blank= True, on_delete= models.CASCADE) #relazione 1 a 1, se customer viene eliminato anche l'user verrà eliminato
    name = models.CharField(max_length=30, null = True)
    email = models.EmailField(max_length = 30,null = True)
    phone = models.CharField(max_length=30, null = True)
    signUpDate = models.DateTimeField(auto_now_add= True)
    propic = models.ImageField(default="pro.jpg",null = True, blank=True)

    def __str__(self):
        return self.name

        #('Disegno', 'Disegno'),
        #('Acquerelli','Acquerelli'),
        #('Pittura ad olio', 'Pittura ad olio'),
        #('Scultura','Scultura'),

class Tag(models.Model):
    name = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY= (
        ('Libri', 'Libri'),
        ('Strumenti','Strumenti'),
        ('Poster','Poster'),

    )
    name = models.CharField(max_length=30, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=5 ,null = True)
    description = models.CharField(max_length=3000, null = True)
    category = models.CharField(max_length=30, null = True,choices=CATEGORY)
    tags = models.ManyToManyField(Tag)
    img = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url





class Order(models.Model):
    STATUS =(
        ('In elaborazione','In elaborazione'),
        ('Spedito','Spedito'),
        ('Consegnato', 'Consegnato'),
    )
    customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL)
    #product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) ####
    date = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=200, null= True, choices=STATUS, default='In elaborazione')
    complete = models.BooleanField(default=False, null=True, blank = False)
    transaction_id = models.CharField(max_length=200, null= True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum ([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

