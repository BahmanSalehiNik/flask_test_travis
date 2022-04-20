from tests.base_test import BaseTest
from models.store import StoreModel
import json


class TestStore(BaseTest):
    def test_store_crud(self):
        with self.app.test_client() as client:
            with self.app_context():
                res = client.post('/store/test')
                self.assertEqual(res.status_code, 201)

                store = StoreModel.find_by_name('test')
                self.assertIsNotNone(store)
                self.assertEqual(store.store_name, 'test')

                res_put = client.put('store/test', data=json.dumps({'new_name': 'test_2'}),
                                     headers={'Content-Type': 'application/json'})
                self.assertEqual(res_put.status_code, 200)
                store = StoreModel.find_by_name('test_2')
                self.assertIsNotNone(store)
                self.assertEqual(store.store_name, 'test_2')

                store = StoreModel.find_by_name('test')
                self.assertIsNone(store)

                res_del = client.delete('store/test_2', headers={'Content-Type': 'application/json'})
                self.assertEqual(res_del.status_code, 200)
