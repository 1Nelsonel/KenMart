from urllib import request
from django.shortcuts import render
from estore.models import Product

# Create your views here.
def index(request):
        return render(request, 'index.html')

def shop(request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'shop.html', context)

def product(request,pk):
        product = Product.objects.get(id=pk)
        context = {'product': product}
        return render(request, "product.html", context)

def contact(request):
        return render(request, 'contact.html') 

def about(request):
        return render(request, 'about.html')

def blog(request):
        return render(request, 'blog.html')

def blog_single(request):
        return render(request, 'blog-single.html')
        
def agents(request):
        return render(request, 'agents.html')
def agent_single(request):
        return render(request, 'agent-single.html')


