from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from estore.models import Product, Category

# Create your views here.
def index(request):
        return render(request, 'estore/index.html')

def shop(request):
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        products = Product.objects.filter(
        Q(product_name__icontains=q) |
        Q(category__category_name__icontains=q) |
        Q(sub_sub_category__sub_sub_category_name__icontains=q) |
        Q(sub_category__sub_category_name__icontains=q) |
        # Q(host__username__icontains=q) |
        Q(description__icontains=q)
    )

        categories = Category.objects.all()

        context = {'products': products, 'categories': categories}
        return render(request, 'estore/shop.html', context)

def product(request,pk):
        product = Product.objects.get(id=pk)
        context = {'product': product}
        return render(request, "estore/product.html", context)

def contact(request):
        return render(request, 'estore/contact.html') 

def about(request):
        return render(request, 'estore/about.html')

def blog(request):
        return render(request, 'estore/blog.html')

def blog_single(request):
        return render(request, 'estore/blog-single.html')
        
def agents(request):
        return render(request, 'estore/agents.html')
def agent_single(request):
        return render(request, 'estore/agent-single.html')


