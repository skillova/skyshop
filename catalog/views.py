from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product


class CatalogListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"You have new message from {name}({email}): {message}")
    return render(request, "catalog/contacts.html")


class ProductDetailView(DetailView):
    model = Product
