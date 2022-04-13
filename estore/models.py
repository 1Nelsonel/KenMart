from django.db import models

# Create your models here. 
# Main Category
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name



# Sub_Category
class Sub_Category(models.Model):
    sub_category_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name



# Sub_Sub_Category
class Sub_Sub_Category(models.Model):
    sub_sub_category_name = models.CharField(max_length=50)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_sub_category_name


    
    
# product
class Product(models.Model):   
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    sub_sub_category = models.ForeignKey(Sub_Sub_Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    image1 = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    description = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    num_stars = models.IntegerField()

    def __str__(self):
        return self.product_name


