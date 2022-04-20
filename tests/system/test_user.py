from tests.base_test import BaseTest
import json
from models.user import UserModel


class TestUser(BaseTest):
    def test_register_user(self):
        with self.app.test_client() as client:
            with self.app_context():
                request = client.post('/register', data={'username': 'bahman', 'password': '123456'})

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('bahman'))
                self.assertEqual(json.loads(request.data), {'message': 'user created successfully'})

    def test_register_and_login(self):
        with self.app.test_client() as client:
            with self.app_context():
                res = client.post('/register', data={'username': 'bahman', 'password': '123456'})
                self.assertEqual(res.status_code, 201)
                jwt_res = client.post('/auth',
                                      json={'username': 'bahman', 'password': '123456'},
                                      headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(jwt_res.data).keys())
                self.assertEqual(jwt_res.status_code, 200)

    def test_register_duplicate_user(self):
        with self.app.test_client() as client:
            with self.app_context():
                res = client.post('/register', data={'username': 'bahman', 'password': '123456'})
                self.assertEqual(res.status_code, 201)

                res = client.post('/register', data={'username': 'bahman', 'password': '12345678'})
                self.assertEqual(res.status_code, 400)
