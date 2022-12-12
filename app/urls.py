from django.urls import path, include
from E_shop.views import *
from . import views
from app.views import Contact_Page


urlpatterns = [
    path('', index, name='index'),
    path('contact_us', views.Contact_Page, name='contact_page'),
    path('checkout/', views.CheckOut, name='checkout'),
    path('order/', views.Your_Order, name='order'),
    path('product/', views.Product_page, name='product')
]
