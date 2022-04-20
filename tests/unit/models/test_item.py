import unittest
from models.item import ItemModel


class TestItem(unittest.TestCase):
    def test_create_valid_item(self):
        item = ItemModel('laptop', 2000, 1)
        self.assertEqual(item.name, 'laptop', 'Item name creation error')
        self.assertEqual(item.price, 2000)
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('PC', 3000, 1)
        self.assertEqual(item.json(), {'name': 'PC', 'price': 3000, 'store_id': 1})


if __name__ == '__main__':
    unittest.main()