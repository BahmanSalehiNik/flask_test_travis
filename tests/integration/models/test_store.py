from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel('store_test')

            self.assertIsNone(StoreModel.find_by_name('store_test'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('store_test'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('store_test'))

    def test_create_valid_store_with_empty_items(self):
        store = StoreModel('test')
        self.assertEqual(store.items.all(), [])

    def test_adding_item_to_store(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('jeans', 10, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'jeans')

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertEqual(expected, store.json())

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('jeans', 10, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'test',
                'items': [{'name':'jeans', 'price': 10, 'store_id': 1}]
            }

            self.assertEqual(store.json(), expected)