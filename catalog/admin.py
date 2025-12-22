from django.contrib import admin
from django.utils.html import format_html

from .models import Advantage, Category, ImageGallery, Product, ContactInfo


class ImageGalleryInline(admin.TabularInline):
    """Inline редактор для изображений галереи товара."""
    model = ImageGallery
    extra = 1
    fields = ('image', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if not obj.image:
            return '-'
        try:
            url = obj.image.url
        except Exception:
            return '-'
        return format_html('<img src="{}" style="max-height:80px;" />', url)

    image_tag.short_description = 'Предпросмотр'


class AdvantageInline(admin.TabularInline):
    """Inline редактор для преимуществ товара."""
    model = Advantage
    extra = 1
    fields = ('description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'product_count',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('product_count',)
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'product_count')
        }),
    )

    def image_tag(self, obj):
        """Показывает предпросмотр изображения категории."""
        if not obj.image:
            return '-'
        try:
            url = obj.image.url
        except Exception:
            return '-'
        return format_html('<img src="{}" style="max-height:100px;" />', url)

    image_tag.short_description = 'Изображение'

    def product_count(self, obj):
        """Показывает количество товаров в категории."""
        count = obj.products.count()
        return f'{count} товаров'

    product_count.short_description = 'Товаров в категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'slug',
                    'image_tag', 'gallery_count')
    list_filter = ('category', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_tag', 'gallery_count')
    ordering = ('category', 'name')
    list_editable = ('price',)
    inlines = (ImageGalleryInline, AdvantageInline)

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'category', 'price', 'image', 'image_tag')
        }),
        ('Описание и состав', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
        ('Статистика', {
            'fields': ('gallery_count',),
            'classes': ('collapse',)
        }),
    )

    def image_tag(self, obj):
        """Показывает предпросмотр основного изображения товара."""
        if not obj.image:
            return '-'
        try:
            url = obj.image.url
        except Exception:
            return '-'
        return format_html('<img src="{}" style="max-height:80px;" />', url)

    image_tag.short_description = 'Изображение'

    def gallery_count(self, obj):
        """Показывает количество изображений в галерее."""
        count = obj.gallery_images.count()
        return f'{count} фото'

    gallery_count.short_description = 'Изображений в галерее'


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'whatsapp_number', 'email')
    search_fields = ('phone_number', 'whatsapp_number', 'email')
    ordering = ('phone_number',)
    fieldsets = (
        (None, {
            'fields': ('phone_number', 'whatsapp_number', 'email')
        }),
    )

    def save_model(self, request, obj, form, change):
        """Автоматически очищает номер WhatsApp от лишних символов."""
        if obj.whatsapp_number:
            # Оставляем только цифры и +
            obj.whatsapp_number = ''.join(
                c for c in obj.whatsapp_number if c.isdigit() or c == '+')
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        """Ограничивает добавление новых записей, разрешая только одну запись."""
        if ContactInfo.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        """Запрещает удаление записей."""
        return False
