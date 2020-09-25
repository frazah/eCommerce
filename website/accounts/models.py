from django.db import models

# Create your models here.


#qui scriviamo le tabelle del database

class Customer(models.Model):
    name = models.CharField(max_length=30, null = True)
    email = models.EmailField(max_length = 30,null = True)
    phone = models.CharField(max_length=30, null = True)
    signUpDate = models.DateTimeField(auto_now_add= True)

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
        ('Opere', 'Opere'),
        ('Strumenti','Strumenti'),

    )
    name = models.CharField(max_length=30, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=5 ,null = True)
    description = models.CharField(max_length=3000, null = True)
    category = models.CharField(max_length=30, null = True,choices=CATEGORY)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name






class Order(models.Model):
    STATUS =(
        ('In elaborazione','In elaborazione'),
        ('Spedito','Spedito'),
        ('Consegnato', 'Consegnato'),
    )
    user = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=200, null= True, choices=STATUS)

    def __str__(self):
        return self.product.name

