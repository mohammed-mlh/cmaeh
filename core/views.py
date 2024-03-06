from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from core.models import ContactMessage, Product, Category, Order
from config.models import Config


def index(request):
  products = Product.objects.all().filter(is_featured=True)
  categories = Category.objects.all().filter()
  config = Config.objects.first()
  return render(request, 'core/index.html', {
    'products': products,
    'categories': categories,
    'config': config
    })

def products(request):
  products = Product.objects.all().filter(is_featured=True)
  return render(request, 'core/products.html', {
    'products': products,
    })

def product_details(request: HttpRequest, slug: str):
    product = Product.objects.get(slug=slug)
    colors = product.colors.split(',') if product.colors else []
    sizes = product.sizes.split(',') if product.sizes else []
    
    if request.method == 'POST':
        # Handle form submission manually
        color = request.POST.get('color')
        size = request.POST.get('size')
        name = request.POST.get('name')
        city = request.POST.get('city')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided

        # Create a new order object
        order = Order.objects.create(
            product=product,
            color=color,
            size=size,
            quantity=quantity,
            city=city,
            name=name,
            address=address,
            phone_number=phone_number,
        )

        # Additional logic can be added here, such as calculating total price, etc.

        return HttpResponse('sucess')  # Redirect to a success page after order submission

    else:
        # Render the form with initial data
        initial_form_data = {'quantity': 1}
        context = {
            'product': product,
            'colors': colors,
            'sizes': sizes,
            'initial_form_data': initial_form_data,
        }

    return render(request, 'core/product_details.html', context)


def contact_form(request: HttpRequest):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        # Create a new ContactMessage object and save it to the database
        ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            message=message
        )

        # Redirect to a success page or any other page
        return HttpResponse('<h1 class="w-full font-bold text-center text-xl">Message envoyé avec succéss</h1>')  # Replace 'success_page' with the URL name of your success page

    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')