from django.contrib import admin
from .models import Product, Order, ContactMessage

admin.site.site_title = 'CMAEH'
admin.site.site_header = 'CMAEH Sytem'



admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ContactMessage)