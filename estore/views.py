from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request, 'index.html')
def shop(request):
        return render(request, 'shop.html')
def product(request):
        return render(request, 'product.html')
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


