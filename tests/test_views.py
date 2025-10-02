from django.test import TestCase
from LittleLemonAPI.views import SingleMenuItem
from LittleLemonAPI.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ceviche",price=8,inventory=10)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(str(items[0]),"Ceviche:8" )

