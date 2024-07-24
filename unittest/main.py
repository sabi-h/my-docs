"""Tutorial for unittesting.

https://docs.python.org/3/library/unittest.html#.
"""

import datetime
import unittest


class TooManyBoardsError(Exception):
    """Custom Exceptions for too many boards."""

    def __init__(self):
        message = f"'Cart cannot have more than 4 surfboards in it!'"
        super().__init__(message)


class CheckoutDateError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = "" if quantity == 1 else "s"
            return f"Successfully added {quantity} surfboard{suffix} to cart!"

    def set_checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        else:
            self.checkout_date = date

    def apply_locals_discount(self):
        self.locals_discount = True


class TestShoppingCart(unittest.TestCase):
    """Tests for code above."""

    def setUp(self):
        """Run before every test."""
        self.cart = ShoppingCart()

    def test_add_surfboards(self):
        test_values = {1: 1, 2: 3}
        for value, result in test_values.items():
            with self.subTest(value):
                self.cart.add_surfboards(value)
                self.assertEqual(
                    self.cart.num_surfboards,
                    result,
                    f"Successfully added {value} surfboard to cart!",
                )

    def test_add_surfboards_adds_5(self):
        self.assertRaises(TooManyBoardsError, self.cart.add_surfboards, 5)

    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def test_set_checkout_date(self):
        date = datetime.datetime.now() + datetime.timedelta(days=1)
        self.cart.set_checkout_date(date)
        self.assertEqual(self.cart.checkout_date, date)

    def test_set_checkout_date_error(self):
        date = datetime.datetime.now() - datetime.timedelta(days=1)
        self.assertRaises(CheckoutDateError, self.cart.set_checkout_date, date)


if __name__ == "__main__":
    """run in terminal using:
        python main.py
    """
    unittest.main()
