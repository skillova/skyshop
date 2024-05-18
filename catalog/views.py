from django.shortcuts import render
from catalog.models import Product


# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')
