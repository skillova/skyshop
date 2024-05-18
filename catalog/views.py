from django.shortcuts import render, get_object_or_404
from catalog.models import Product


# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/products_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')


def product_info(requests, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(requests, 'catalog/product_info.html', context)
