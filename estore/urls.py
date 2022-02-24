from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # app homepage
    path('shop', views.shop, name='shop'),
    path('property_single', views.property_single, name='property_single'), 
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'), 
    path('blog_single', views.blog_single, name='blog-single'), 
    path('agent_single', views.agent_single, name='agent_single'),  
    ]
