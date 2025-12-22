from .models import Category, ContactInfo


def site_context(request):
    """
    Контекстный процессор для глобальных данных сайта.
    """
    return {
        'categories': Category.objects.all(),
        'contact_info': ContactInfo.objects.first(),
    }
