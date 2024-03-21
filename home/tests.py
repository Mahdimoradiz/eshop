from django.test import TestCase
from home.models import Setting

class SettingTest(TestCase):
    def setUp(self):
        Setting.objects.create(title="Hello test")
        