import unittest

from pricing import apply_coupon, apply_discount, total


class PricingTest(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(apply_discount(1000, 10), 900)

    def test_discount_rejects_out_of_range(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, 101)

    def test_coupon_save10(self):
        self.assertEqual(apply_coupon(1000, "SAVE10"), 900)

    def test_coupon_save20(self):
        self.assertEqual(apply_coupon(1000, "SAVE20"), 800)

    def test_coupon_rejects_unknown_code(self):
        with self.assertRaises(ValueError):
            apply_coupon(1000, "UNKNOWN")

    def test_total(self):
        self.assertEqual(total([100, 250]), 350)


if __name__ == "__main__":
    unittest.main()
