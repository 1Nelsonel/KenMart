from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request, 'index.html')
def shop(request):
        return render(request, 'property-grid.html')
def property_single(request):
        return render(request, 'property-single.html')
def contact(request):
        return render(request, 'contact.html')   
def about(request):
        return render(request, 'about.html')
def blog(request):
        return render(request, 'blog-grid.html')
def blog_single(request):
        return render(request, 'blog-single.html')
def agent_single(request):
        return render(request, 'agent-single.html')