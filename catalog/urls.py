from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, contacts, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
]
