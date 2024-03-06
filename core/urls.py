from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('produits/', views.products, name='products'),
  path('product/<slug:slug>', views.product_details, name='product_details'),
  path('contactez-nous/', views.contact_form, name='contact'),
  path('apropos/', views.about, name='about'),
]
