import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models.category import Category

User = get_user_model()
test_user = {
    "username": "Tester",
    "email": "testing@email.com",
    "password": "sh1th3@d"
}

client = APIClient()

class AdvertModuleTestCase(TestCase): 
    def setUp(self): 
        User.objects.create(**test_user).save()
        Category.objects.create(title="Fashion")


    def test_creating_ads(self): 
        tUser = User.objects.get(email="testing@email.com")
        token = RefreshToken.for_user(tUser)
        access_token = str(token.access_token)

        ad_data = {
             "title": "New Ad",
            "description": "This is my awesome ad." ,
            "category": 1,
            "tags": json.dumps(["bla"])
        }
        client.credentials(HTTP_AUTHORIZATION='JWT ' + access_token)
        response = client.post('/advert/create/', {**ad_data})
        self.assertEqual(response.data['title'], ad_data['title'])


    def test_listing_all_ads(self):
        response = client.get('/advert/')
        # self.assertEqual(response.data, [])