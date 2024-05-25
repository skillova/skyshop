from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


class CatalogListView(ListView):
    model = Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
