from django.test import TestCase, Client
from django.urls import reverse, resolve
from api.views import addNumbers, multiplyNumbers


class TestUrls(TestCase): # Check whether the urls are resolved
  def test_addNumbers_url_is_resolved(self):
    url = reverse(addNumbers)
    self.assertEquals(resolve(url).func, addNumbers)
  def test_multiplyNumbers_url_is_resolved(self):
    url = reverse(multiplyNumbers)
    self.assertEquals(resolve(url).func, multiplyNumbers)

class TestViews(TestCase): # Check whether the views properly work
  def SetUp(self):
    self.client = Client()
  def test_addNumbers_GET(self): # Test for the GET method
    response = self.client.get(reverse(addNumbers))
    self.assertEquals(response.status_code, 200) # Status code 200 indicates the method specified is successfully called
  def test_addNumbers_POST(self): # Test for the POST method
    response = self.client.post(reverse(addNumbers), {'numbers': [1, 2, 3]})
    self.assertEquals(response.status_code, 200)
  def test_multiplyNumbers_GET(self):
    response = self.client.get(reverse(multiplyNumbers))
    self.assertEquals(response.status_code, 200)
  def test_multiplyNumbers_POST(self):
    response = self.client.post(reverse(multiplyNumbers), {'numbers': [1, 2, 3]})
    self.assertEquals(response.status_code, 200)