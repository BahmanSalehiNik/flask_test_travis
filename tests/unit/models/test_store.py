from models.store import StoreModel
from tests.base_test import BaseTest


class TestStoreModel(BaseTest):
    def test_create_valid_store(self):
        store = StoreModel('Sony')
        self.assertEqual(store.store_name, 'Sony')