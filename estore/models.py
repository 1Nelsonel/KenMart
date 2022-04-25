from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# Main Category


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


# Sub_Category
class Sub_Category(models.Model):
    sub_category_name = models.CharField(max_length=50)
    category = models.ManyToManyField(
        Category, related_name='category', blank=True)

    def __str__(self):
        return self.sub_category_name


# Sub_Sub_Category
class Sub_Sub_Category(models.Model):
    sub_sub_category_name = models.CharField(max_length=50)
    sub_category = models.ManyToManyField(
        Sub_Category, related_name='sub_category', blank=True)

    def __str__(self):
        return self.sub_sub_category_name

# customer


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# product


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    sub_sub_category = models.ForeignKey(Sub_Sub_Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    description = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    num_stars = models.FloatField(default=0, validators=[MaxValueValidator(10),MinValueValidator(1)])

    class Meta:
        ordering = ['-updated', '-release_date']

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
    Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
