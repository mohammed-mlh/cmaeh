from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

class Category(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  image = models.ImageField(upload_to='category_images/')
  slug = AutoSlugField(populate_from='title', unique=True, blank=True)

  def __str__(self):
    return self.title

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
  title = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  past_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  description = models.TextField()
  colors = models.CharField(max_length=100, blank=True)
  sizes = models.CharField(max_length=100, blank=True)
  available_quantity = models.PositiveIntegerField(default=0)
  is_featured = models.BooleanField(default=False)
  slug = AutoSlugField(populate_from='title', unique=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

# class ProductsVariant(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
#     name = models.CharField(max_length=100)
#     options = models.TextField()  # Keeping options as a TextField

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.product.title} - {self.name}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image of {self.product.title}"


class Order(models.Model):
  name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=15)  # Assuming phone numbers can be represented as strings
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  color = models.CharField(max_length=50, null=True, blank=True)  # Text field to store selected options
  size = models.CharField(max_length=50, null=True, blank=True)  # Text field to store selected options

  def __str__(self):
    return f"Order #{self.pk} - {self.name}"
  

class ContactMessage(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=20, blank=True, null=True)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name} - {self.created_at}'