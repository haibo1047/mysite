from django.test import TestCase,Client
from django.urls import reverse

from django.http import Http404

# Create your tests here.

from .models import Toy
from django.utils import timezone

class ToyTest(TestCase):
    def test1(self):
        cur = Toy('1',100,timezone.now())
        self.assertIsNotNone(cur)

    def testHomeView(self):
        client = Client()
        url = reverse("home1")
        response = client.get(url)
        self.assertNotEqual(response.status_code,Http404)