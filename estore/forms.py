from django.forms import ModelForm
from .models import Product, User
from django.contrib.auth.forms import UserCreationForm



# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
        # exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name']
        