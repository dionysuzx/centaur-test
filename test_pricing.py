import unittest

from pricing import apply_discount, total


class PricingTest(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(apply_discount(1000, 10), 900)

    def test_discount_rejects_out_of_range(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, 101)

    def test_total(self):
        self.assertEqual(total([100, 250]), 350)


if __name__ == "__main__":
    unittest.main()
