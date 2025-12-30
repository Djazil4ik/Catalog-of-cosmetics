from django.contrib.auth.models import User
from django.urls import reverse
from catalog.models import ImageGallery, Advantage
from django.test import TestCase
from catalog.models import Product, Category
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.


class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Кремы',
            slug='kremy'
        )

        self.product = Product.objects.create(
            name='Увлажняющий крем',
            category=self.category,
            price=199.99,
            slug='uvlazhnyayushchiy-krem'
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Увлажняющий крем')

    def test_product_has_price(self):
        self.assertGreater(self.product.price, 0)


class ProductRelationsTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Сыворотки',
            slug='syvorotki'
        )

        self.product = Product.objects.create(
            name='Vitamin C',
            category=self.category,
            price=299.99,
            slug='vitamin-c'
        )

        self.image = SimpleUploadedFile(
            "test.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        

    def test_gallery_images_count(self):
        ImageGallery.objects.create(product=self.product)
        ImageGallery.objects.create(product=self.product)

        self.assertEqual(self.product.gallery_images.count(), 2) #type: ignore

    def test_advantages(self):
        Advantage.objects.create(
            product=self.product,
            description='Без парабенов'
        )

        self.assertEqual(self.product.advantages.count(), 1) #type: ignore


class ProductViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Маски',
            slug='maski'
        )

        self.product = Product.objects.create(
            name='Глиняная маска',
            category=self.category,
            price=149.99,
            slug='glinyanaya-maska'
        )

    def test_product_detail_view(self):
        url = reverse('catalog:product_detail', args=[self.product.slug])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Глиняная маска')


class AdminTest(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@test.com'
        )
        self.client.login(username='admin', password='admin123')

    def test_admin_product_page(self):
        response = self.client.get('/admin/catalog/product/')
        self.assertEqual(response.status_code, 200)
