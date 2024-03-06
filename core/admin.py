from django.contrib import admin
from .models import Category, Product, ProductImage, Order, ContactMessage

admin.site.site_title = 'COD System'
admin.site.site_header = 'COD Sytem'

class ProductsImageInline(admin.TabularInline):
  model = ProductImage

class ProductAdmin(admin.ModelAdmin):
  inlines = [
    ProductsImageInline,
  ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(ContactMessage)