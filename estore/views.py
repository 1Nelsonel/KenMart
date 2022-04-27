from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from estore.models import Product, Category, Sub_Category, Sub_Sub_Category, Customer, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Product, User
from .forms import UserForm
# Create your views here.


def index(request):
    return render(request, 'estore/index.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('shop')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid User')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            messages.error(request, 'Invalid login credentials')
    context = {'page': page}
    return render(request, 'estore/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('index')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User registered')
            return redirect('shop')
        else:
            messages.error(request, 'Failed, Please Try Again.')
            
        
    return render(request, 'estore/login_register.html', {'form': form})



def shop(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(category__category_name__icontains=q) |
        Q(sub_sub_category__sub_sub_category_name__icontains=q) |
        Q(sub_category__sub_category_name__icontains=q) |
        # Q(host__username__icontains=q) |
        Q(description__icontains=q)
    )

    categories = Category.objects.all()
    paginator = Paginator(products, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': products,
        'categories': categories, 'page_obj': page_obj}
    return render(request, 'estore/shop.html', context)


def product(request, pk):

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


# cart add, remove, clear, increment, decrement

@login_required(login_url="/admin/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    
    return redirect("shop")


@login_required(login_url="/admin/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    messages.info(request, "Item cleared from cart")
    return redirect("cart_detail")


@login_required(login_url="/admin/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.info(request, "Product increased in cart")
    return redirect("cart_detail")


@login_required(login_url="/admin/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    messages.info(request, "Product decreased in cart")
    return redirect("cart_detail")


@login_required(login_url="/admin/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.info(request, "Product cleared cart")
    return redirect("cart_detail")


def cart_detail(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}

    context = {'items': items, 'order': order}
    return render(request, 'estore/cart_detail.html', context)

    pass

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
    context = {'items': items, 'order': order}
    return render(request, 'estore/checkout.html', context)
