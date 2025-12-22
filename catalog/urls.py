from django.urls import path

from .views import CatalogListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog_list'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
