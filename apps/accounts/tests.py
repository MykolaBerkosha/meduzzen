
from django.contrib.auth.models import User

from rest_framework.test import APITestCase


class ListAPITestCase(APITestCase):

    def setUp(self):

        self.admin = User.objects.create_user('admin', is_staff=True)
        self.client.force_authenticate(self.admin)

    def test_get_endpoint(self):

        User.objects.create_user('user', first_name='User')

        response = self.client.get('/api/v1/accounts/')

        self.assertEqual(response.status_code, 200)

        users = response.data

        self.assertEqual(len(users), 2)

        self.assertEqual(users[0]['username'], 'admin')
        self.assertEqual(users[1]['username'], 'user')

    def test_post_endpoint(self):

        response = self.client.post('/api/v1/accounts/', {
            'username': 'user',
            'password': '123',
            'first_name': 'User'
        })

        user = response.data['user']

        self.assertEqual(user['username'], 'user')
        self.assertEqual(user['first_name'], 'User')


class ObjectAPITestCase(APITestCase):

    def setUp(self):

        self.admin = User.objects.create_user('admin', is_staff=True)
        self.client.force_authenticate(self.admin)

    def test_delete_endpoint(self):

        user = User.objects.create_user('user', first_name='User')

        response = self.client.delete('/api/v1/accounts/{}/'.format(user.pk))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['status'], 'User removed')

        self.assertEqual(User.objects.count(), 1)
