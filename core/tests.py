import requests
import httpretty

from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
 

class TestApp(TestCase):

    def setUp(self):
        self.client = Client()
        self.payload = {}
        self.url = "http://api.musixmatch.com/ws/1.1/track.search"

    def test_Homepage_OK(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertIn("Muzix Recommender can help you search", res.content)

    @httpretty.activate
    def test_POST_works(self):
        # patch
        httpretty.register_uri(httpretty.GET, 
                              self.url, 
                              body='{"track": "I love my baby."}',
                            )

        self.payload = {'q_lyrics': 'love'}
        res = requests.get(self.url, params=self.payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {'track': 'I love my baby.'})
        

