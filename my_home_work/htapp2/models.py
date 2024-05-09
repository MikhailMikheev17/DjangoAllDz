from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(default=None)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Client: {self.name}, email: {self.email}, phone:{self.phone}, address:{self.address},'
                )


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)

    def __str__(self):
        return (f'Product: {self.name}, description: {self.description}, price:{self.price}, rest_quantity:{self.quantity}, '
                f'created_at:{self.created_at}')


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_created=True) # убрать авто для фейковой генерации

    def __str__(self):
        product_names = ', '.join([product.name for product in self.products.all()])
        return (f'Order details: Client name: {self.customer.name}, client phone: {self.customer.phone},'
                f' goods in order: {product_names}, '
                f'total amount: {self.total_amount}')

# Create your models here.
