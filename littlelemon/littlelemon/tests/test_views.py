from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(title="Item1", price=10, inventory=20)
        self.menu_item2 = Menu.objects.create(title="Item2", price=15, inventory=30)

    def test_get_all_menu_items(self):
        queryset = Menu.objects.all()
        serialized_queryset = MenuSerializer(queryset, many=True).data
        serialized_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data
        self.assertEqual(serialized_queryset, serialized_data)