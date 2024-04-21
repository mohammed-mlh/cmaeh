from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('company/', views.CompanyView.as_view(), name='company'),
  path('faq/', views.FaqView.as_view(), name='faq'),
  path('checkout/', views.CheckoutView.as_view(), name='checkout'),
  path('order/', views.OrderView.as_view(), name='order'),
  path('product/<slug:slug>', views.ProductView.as_view(), name='product_details'),
  path('add-to-cart/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
  path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
  path('update-quantity/<str:product_id>/', views.UpdateItemQuantityView.as_view(), name='update_item_quantity'),
  path('cart/', views.ViewCart.as_view(), name='view_cart'),
  path('clear-cart/', views.clear_cart, name='clear_cart'),
]
