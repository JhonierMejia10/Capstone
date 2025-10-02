from django.test import TestCase
from LittleLemonAPI.models import Menu

class MenuTest(TestCase):
    def test_instance(self):
        item = Menu.objects.create(title="Lemonade",price=2,inventory=20)
        self.assertEqual(str(item), "Lemonade:2")

