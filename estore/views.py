from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from estore.models import Product, Category, Sub_Category, Sub_Sub_Category, Customer, Order, OrderItem, ShippingAddress

# Create your views here.


def index(request):
    return render(request, 'estore/index.html')


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

@property
def get_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total


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

def total_price(request):
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
