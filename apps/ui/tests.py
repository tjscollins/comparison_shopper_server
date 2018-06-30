from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page
from .models import GroceryList, GroceryItem, User
from apps.product_info.models import Product


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post(
            '/', data={'grocery_item': 'cheese'}
        )

        self.assertIn('Cheese', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
    
    def test_save_groceries(self):
        p1 = Product()
        p1.name = 'mushrooms'
        p2 = Product()
        p2.name = 'milk'
        p3 = Product()
        p3.name = 'coffee'
        p1.save()
        p2.save()
        p3.save()

        g1 = GroceryItem()
        g1.product = p1
        g2 = GroceryItem()
        g2.product = p2
        g3 = GroceryItem()
        g3.product = p3
        g1.save()
        g2.save()
        g3.save()

        user = User()
        user.first_name = "Tom"
        user.last_name = 'Riddle'
        user.email = 'iamlordvoldemort@hogwarts.com'
        user.preferred_location = 'Platform 9 3/4'
        user.save()

        glist = GroceryList()
        glist.user = user
        glist.save()
        glist.items.set([g1, g2, g3])
        glist.save()

        self.assertIn(g1, GroceryItem.objects.all())
        self.assertIn(g2, GroceryItem.objects.all())
        self.assertIn(g3, GroceryItem.objects.all())
        self.assertIn(glist, GroceryList.objects.all())
