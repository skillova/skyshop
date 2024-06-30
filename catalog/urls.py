from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogListView,
    contacts,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, CategoryListView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_detail/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update_product"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"),
    path('category/', CategoryListView.as_view(), name='category'),
]
