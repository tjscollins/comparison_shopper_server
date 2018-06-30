from django.test import TestCase
from django.urls import resolve
from product_info.models import Product


# Create your tests here.
class ProductTest(TestCase):

    def test_saving_and_retrieving_products(self):
        first_product = Product()
        first_product.name = 'Kraft Singles'
        first_product.upc = '1234567890123'
        first_product.save()

        second_product = Product()
        second_product.name = 'Breyer\'s Vanilla Ice-cream'
        second_product.upc = '0987654321123'
        second_product.save()

        saved_products = Product.objects.all()
        self.assertEqual(saved_products.count(), 2)

        first_saved_product = saved_products[0]
        second_saved_product = saved_products[1]

        self.assertEqual(first_product.name, first_saved_product.name)
        self.assertEqual(second_product.name, second_saved_product.name)

