from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='ЧПУ (slug)')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара')
    description = CKEditor5Field(config_name='extends', verbose_name='Описание товара')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение товара')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='ЧПУ (slug)')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery_images', verbose_name='Товар')
    image = models.ImageField(verbose_name='Изображение галереи')

    def __str__(self):
        return f"Image for {self.product.name}"
    
class Advantage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='advantages', verbose_name='Товар')
    description = models.CharField(max_length=255, verbose_name='Преимущество')

    def __str__(self):
        return f"Advantage for {self.product.name}: {self.description}"


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    whatsapp_number = models.CharField(max_length=20, verbose_name='Номер WhatsApp', help_text='Формат: +998901234567 (только цифры и +, без пробелов и дефисов)')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return f"Contact Info: {self.phone_number}, {self.whatsapp_number}, {self.email}"