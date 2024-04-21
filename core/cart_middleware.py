from .models import Product

class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cart_items = request.session.get('cart_items', [])

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

        request.cart_data = {
            'cart_products': cart_products,
            'total_quantity': total_quantity,
            'total_price': total_price
        }

        response = self.get_response(request)
        return response
