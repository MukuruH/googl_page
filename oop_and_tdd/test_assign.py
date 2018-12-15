import unittest
from assign import create_quick_order, create_standard_order, delivered, StandardOrder, QuickOrder


class TestOrder(unittest.TestCase):
    def test_change_extra_dime(self):
        create_quick_order('Bag', 18, 300000)
        order = delivered[-1]

        self.assertIsInstance(order, QuickOrder)
        order.change_extra_dime(400000)
        self.assertEqual(order.extra_dime, 400000)

    def test_create_quick_order(self):
        self.assertRaises(ValueError )
        pass

    def test_create_standard_order(self):
        pass

    def test_create_quick_order_with_little_extra_dime(self):
        pass

    def test_create_quick_order_with_exceeded_deadline(self):
        pass