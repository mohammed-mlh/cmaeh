from django import forms
from .models import Order, ContactMessage

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'product', 'name', 'phone_number', 'city', 'address', 'color', 'size']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'phone_number', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }