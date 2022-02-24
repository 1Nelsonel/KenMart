from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # app homepage
    path('shop', views.shop, name='shop'),
    path('product', views.product, name='product'), 
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'), 
    path('blog_single', views.blog_single, name='blog_single'),
    path('agents', views.agents, name='agents'), 
    path('agent_single', views.agent_single, name='agent_single'),  
    ]
