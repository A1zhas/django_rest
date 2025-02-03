from django.test import Client, TestCase
from faker import Faker
from usersapp.models import BlogUser

class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Что можем еще проверить
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        # Post запрос
        response = self.client.post('/contact/',
                                    {'name': self.fake.name(), 'message': self.fake.text(),
                                     'email': self.fake.email()})
        self.assertEqual(response.status_code, 302)

        # какие данные передаютс в контексте
        response = self.client.get('/')
        self.assertTrue('posts' in response.context)
        #response.context['name']

    def test_login_required(self):
        BlogUser.objects.create_user(username='test_user', email='test@test.com', password='Aaaa1234')
        # Он не вошел
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)

        # Логиним
        self.client.login(username='test_user', password='Aaaa1234')

        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

        # команды
        # python manage.py runserver
        # python manage.py test
        # coverage run manage.py && coverage report