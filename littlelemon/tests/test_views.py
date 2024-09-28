from django.test import TestCase
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Burger", price=10.99, inventory=50)
        Menu.objects.create(title="Pizza", price=12.99, inventory=30)
        Menu.objects.create(title="Salad", price=7.99, inventory=20)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        expected_data = [
            {'id':2,'title': 'Burger', 'price': '10.99', 'inventory': 50},
            {'id':3,'title': 'Pizza', 'price': '12.99', 'inventory': 30},
            {'id':4,'title': 'Salad', 'price': '7.99', 'inventory': 20},
        ]

        self.assertEqual(serializer.data, expected_data)