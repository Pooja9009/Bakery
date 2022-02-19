# Create your tests here.
from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cakes.views import category_form, get_category, update_category, contact_form
from cakes.models import Category
from cakes.forms import MessageForm

# Create your tests here.
class TestURLs(SimpleTestCase):
    def test_category_form(self):
        url = reverse('category_form')
        self.assertEquals(resolve(url).func, category_form)

    def test_get_category(self):
        url = reverse('get_category')
        self.assertEquals(resolve(url).func, get_category)

    def test_update_category(self):
        url = reverse('update_category', args=['1'])
        self.assertEquals(resolve(url).func, update_category)

    def test_contact_us(self):
        url = reverse('contact_us')
        self.assertEquals(resolve(url).func, contact_form)



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.show_category_url = reverse('show_categories')
        self.about_url = reverse('about_us')
    def test_show_category(self):
        response = self.client.get(self.show_category_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakes/show_categories.html')
    def test_about_us(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakes/about.html')


class TestModels(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            category_name = 'Category 1'

        )
    def test_category_model(self):
        self.assertEquals(self.category1.category_name, 'Category 1')

class TestForms(SimpleTestCase):
    def test_message_form_is_valid(self):
        form = MessageForm(data={
            'name': 'ritika',
            'email': 'ritika@gmail.com',
            'phone': 987654321,
            'message': 'message 123'

        })
        self.assertTrue(form.is_valid())

    def test_category_form_no_data(self):
        form = MessageForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
        