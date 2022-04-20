from models.item import ItemModel
from tests.base_test import BaseTest
import unittest
from models.store import StoreModel


class TestItem(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel('Test')
            store.save_to_db()

            item = ItemModel('test', 30.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 200, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.store_name, 'test_store')


if __name__ == '__main__':
    unittest.main()

