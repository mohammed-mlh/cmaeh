from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, DetailView, View
from core.models import Product
from django.contrib import messages
from config.models import Config

class CartContextMixin:
    def get_cart_data(self):
        cart_items = self.request.session.get('cart_items', [])

        cart_products = []
        total_quantity = 0
        total_price = 0

        for item in cart_items:
            product_id = item['product_id']
            quantity = item['quantity']
            product = Product.objects.get(id=product_id)
            subtotal = product.price * quantity

            cart_products.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })

            total_quantity += quantity
            total_price += subtotal

        return {
            'cart_products': cart_products,
            'total_quantity': total_quantity,
            'total_price': total_price
        }


def index(request):
  cart_data = request.cart_data
  print(cart_data)
  products = Product.objects.all().filter(is_featured=True)
  burgers = products.filter(category='burgers')
  sides = products.filter(category='sides')
  drinks = products.filter(category='drinks')
  print(burgers.get(id=2).category)
  config = Config.objects.first()
  return render(request, 'core/index.html', {
    'burgers': burgers,
    'sides': sides,
    'drinks': drinks,
    'config': config
    })

class CompanyView(TemplateView):
    template_name = "core/company.html"

class FaqView(TemplateView):
    template_name = "core/faq.html"

class CheckoutView(TemplateView):
    template_name = "core/checkout.html"

class OrderView(TemplateView):
    template_name = "core/order.html"

class ProductView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "core/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context



class AddToCartView(View):
    def post(self, request, product_id):
        redirect_url = request.META.get('HTTP_REFERER')
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        if quantity < 1:
            messages.error(request, 'Quantity must be at least 1.')
            return redirect(redirect_url)

        # Retrieve cart items from session or create an empty list if not present
        cart_items = request.session.get('cart_items', [])

        # Check if the product is already in the cart
        for item in cart_items:
            if item['product_id'] == product_id:
                item['quantity'] = quantity
                request.session['cart_items'] = cart_items
                messages.success(request, 'Product quantity updated in cart.')
                return redirect(redirect_url)

        # If the product is not in the cart, create a new cart item
        cart_items.append({'product_id': product_id, 'quantity': quantity})
        request.session['cart_items'] = cart_items
        messages.success(request, 'Product added to cart successfully.')
        return redirect(redirect_url)
    
class UpdateItemQuantityView(View):
    def post(self, request, product_id, *args, **kwargs):
        redirect_url = request.META.get('HTTP_REFERER')
        # Get the new quantity from the form data
        new_quantity = int(request.POST.get('commerce-add-to-cart-quantity-input', 1))
        print('ojo',new_quantity)

        # Retrieve the cart from the session
        cart = request.session.get('cart_items', [])

        # Search for the item with the same product ID and update its quantity
        for item in cart:
            if item['product_id'] == product_id:
                item['quantity'] = new_quantity
                break
        else:
            # If the item is not found, return an error or handle it accordingly
            messages.error(request, "Product not found in cart.")
            return redirect('order')  # Replace 'your_orders_url_name' with the name of your orders URL

        # Store the updated cart back into the session
        request.session['cart_items'] = cart

        # Optionally, you can add a success message
        messages.success(request, "Quantity updated successfully.")

        # Redirect to the orders page
        return redirect(redirect_url)  # Replace 'your_orders_url_name' with the name of your orders URL

def remove_from_cart(request, product_id):
    cart_items = request.session.get('cart_items', [])
    cart_items = [item for item in cart_items if item['product_id'] != product_id]
    request.session['cart_items'] = cart_items
    return redirect('cart')



class ViewCart(CartContextMixin, TemplateView):
    template_name = 'core/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_cart_data())
        return context

def clear_cart(request):
    # Clear the cart by removing all items from the session
    request.session['cart_items'] = []
    # Redirect back to the cart page or any other page
    return redirect('/cart')