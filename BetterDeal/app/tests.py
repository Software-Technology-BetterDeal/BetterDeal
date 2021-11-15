from django.test import TestCase, RequestFactory
from .models import *
from django.contrib.auth.models import AnonymousUser, User


# Create your tests here.

class ProductModelTests(TestCase):

    def test___str__(self):
        product = Product(product_name='tej', price=230, supermarket='spar', image_name='tej.jpg')
        result = product.__str__()
        self.assertEqual(product.price, 230)
        self.assertEqual(result, 'tej 230 spar tej.jpg')


class ProfileModelTests(TestCase):

    def test___str__(self):
        user1 = User.objects.create_user('user', 'user@gmail.com', 'pw')
        profile = Profile(user=user1)
        result = profile.__str__()
        self.assertEqual(result, 'user')

class CartModelTests(TestCase):
    def test___str__(self):
        user1 = User.objects.create_user('user4', 'user@gmail.com', 'pw',)
        user1.save()
        profile = Profile.objects.get(user_id=user1.id)
        product1=profile.cart.create(product_name='tej',price=255,supermarket='aldi',image_name='')
        product1.save()
        self.assertEqual(profile.cart.all()[0], product1)

