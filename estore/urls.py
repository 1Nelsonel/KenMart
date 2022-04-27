from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:pk>/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('agents/', views.agents, name='agents'),
    path('agent_single/', views.agent_single, name='agent_single'),
    # path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    # path('update_item/', views.updateItem, name='update_item'),

    # cart

    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/item_clear/', views.item_clear, name='item_clear'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
]
