from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import login_user, profile, change_password
from accounts.models import Profile

# Create your tests here.
class URLTests(SimpleTestCase):
    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)

    def test_profile(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_change_password(self):
        url = reverse('change')
        self.assertEquals(resolve(url).func, change_password)

class TestModels(TestCase):
    def setUp(self):
        self.profile1 = Profile.objects.create(
            username = 'Profile 1',
            phone = 985673644

        )
    def test_profile_model(self):
        self.assertEquals(self.profile1.username, 'Profile 1')


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('bell', 'bell@gmail.com', 'bellpassword')

    def testLogin(self):
        self.client.login(username='bell', password='bellpassword')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)





