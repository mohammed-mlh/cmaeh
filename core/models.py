from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

class Product(models.Model):
  BURGER = 'burgers'
  SIDE = 'sides'
  DRINK = 'drinks'
  
  CATEGORY_CHOICES = [
    (BURGER, 'Burgers'),
    (SIDE, 'Sides'),
    (DRINK, 'Drinks'),
  ]

  title = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  is_featured = models.BooleanField(default=False)
  slug = AutoSlugField(populate_from='title', unique=True, blank=True)
  image = models.ImageField(null=True)
  category = models.CharField(null=True,max_length=100, choices=CATEGORY_CHOICES)

  # Additional information based on category
  # Example: Ingredients for burgers, Size for drinks, etc.
  additional_info = models.CharField(max_length=200, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title
    
class Order(models.Model):
  name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=15)  # Assuming phone numbers can be represented as strings
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)

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
  

class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        # Check if the product is already in the cart
        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                return item  # Return the updated cart item
        # If the product is not in the cart, create a new cart item
        cart_item = CartItem(product=product, quantity=quantity)
        self.items.append(cart_item)
        return cart_item  # Return the newly added cart item

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product.id != product_id]

    def update_quantity(self, product_id, quantity):
        for item in self.items:
            if item.product.id == product_id:
                item.quantity = quantity
                break

    def clear(self):
        self.items.clear()

    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.items)

    @property
    def total_price(self):
        return sum(item.quantity * item.product.price for item in self.items)
