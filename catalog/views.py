from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, RedirectView

from .models import Product


class HomeRedirectView(RedirectView):
    """Перенаправление с корня сайта на каталог (301)."""
    permanent = True
    url = '/catalog/'


class CatalogListView(ListView):
    """Список товаров с пагинацией и возможностью фильтрации по категории.

    Отдельная ответственность: формирование queryset и предоставление контекста.
    """
    model = Product
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset().select_related('category').order_by('name')
        # Поддержка фильтрации по category slug как через GET-параметр, так и через kwargs
        category_slug = self.request.GET.get(
            'category') or self.kwargs.get('category_slug')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.request.GET.get(
            'category') or self.kwargs.get('category_slug')
        return context


class ProductDetailView(DetailView):
    """Просмотр подробной страницы товара по slug.

    Отдельная ответственность: получение объекта и его представление.
    """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        # Явное получение объекта через slug — более явное поведение и легче тестировать
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(Product.objects.select_related('category'), slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.request.GET.get('category') or self.kwargs.get('category_slug')
        return context
