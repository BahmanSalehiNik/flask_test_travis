import json
from models.store import StoreModel
from models.user import UserModel
from models.item import ItemModel
from tests.base_test import BaseTest

headers = {'Content-Type': 'application/json'}


class TestItem(BaseTest):
    def test_create_item(self):
        with self.app.test_client() as client:
            with self.app_context():
                store = StoreModel('test')
                store.save_to_db()
                res = client.post('/item/jeans',
                                  data=json.dumps({'price': 99, 'store_id': 1}),
                                  headers=headers)
                self.assertEqual(res.status_code, 201)
                self.assertIsNotNone(ItemModel.find_by_name('jeans'))

    def test_get_item_no_auth(self):
        with self.app.test_client() as client:
            with self.app_context():
                store = StoreModel('test')
                store.save_to_db()
                res = client.post('/item/jeans',
                                  data=json.dumps({'price': 99, 'store_id': 1}),
                                  headers=headers)
                self.assertEqual(res.status_code, 201)

                res = client.get('/item/jeans')

                self.assertEqual(res.status_code, 401)

    def test_get_item_item_not_found(self):
        with self.app.test_client() as client:
            with self.app_context():
                store = StoreModel('test')
                store.save_to_db()
                res = client.post('/item/jeans',
                                  data=json.dumps({'price': 99, 'store_id': 1}),
                                  headers=headers)
                self.assertEqual(res.status_code, 201)
                user = UserModel('bahman', '123456')
                user.save_to_db()
                auth_res = client.post('/auth', data=json.dumps({'username':'bahman', 'password':'123456'}),
                                       headers=headers)
                self.assertEqual(auth_res.status_code, 200)
                token = json.loads(auth_res.data)['access_token']
                headers['Authorization'] = 'JWT ' + token

                res = client.get('/item/no_jeans', headers=headers)
                self.assertEqual(res.status_code, 404)




    def test_get_item(self):
        with self.app.test_client() as client:
            with self.app_context():
                store = StoreModel('test')
                store.save_to_db()
                res = client.post('/item/jeans',
                                  data=json.dumps({'price': 99, 'store_id': 1}),
                                  headers=headers)
                self.assertEqual(res.status_code, 201)
                user = UserModel('bahman', '123456')
                user.save_to_db()
                auth_res = client.post('/auth', data=json.dumps({'username':'bahman', 'password':'123456'}),
                                       headers=headers)
                self.assertEqual(auth_res.status_code, 200)
                token = json.loads(auth_res.data)['access_token']
                headers['Authorization'] = 'JWT ' + token

                res = client.get('/item/jeans', headers=headers)
                self.assertEqual(res.status_code, 200)

    def test_delete_item(self):
        with self.app.test_client() as client:
            with self.app_context():
                store = StoreModel('test')
                store.save_to_db()
                res = client.post('/item/jeans',
                                  data=json.dumps({'price': 99, 'store_id': 1}),
                                  headers=headers)
                self.assertEqual(res.status_code, 201)
                self.assertIsNotNone(ItemModel.find_by_name('jeans'))
                res = client.delete('item/jeans', headers=headers)
                self.assertEqual(res.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'}, json.loads(res.data))
                self.assertIsNone(ItemModel.find_by_name('jeans'))

    def test_create_duplicate_item(self):
        with self.app.test_client() as client:
            with self.app_context():
                store = StoreModel('test')
                store.save_to_db()
                res = client.post('/item/jeans',
                                  data=json.dumps({'price': 99, 'store_id': 1}),
                                  headers=headers)
                self.assertEqual(res.status_code, 201)
                self.assertIsNotNone(ItemModel.find_by_name('jeans'))

                res = client.post('/item/jeans',
                                  data=json.dumps({'price': 99, 'store_id': 1}),
                                  headers=headers)

                self.assertEqual(res.status_code, 400)
                self.assertIsNotNone(ItemModel.find_by_name('jeans'))

    def test_put_update_item(self):
        pass

    def test_item_list(self):
        pass
