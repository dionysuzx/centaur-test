import unittest

from pricing import apply_coupon, apply_discount, refund, total


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



class LoyaltyTest(unittest.TestCase):
    def test_one_point_per_whole_dollar(self):
        from pricing import loyalty_points

        self.assertEqual(loyalty_points(1999), 19)

    def test_whole_dollar_boundaries(self):
        from pricing import loyalty_points

        for total_cents, expected in [(0, 0), (99, 0), (100, 1), (2000, 20)]:
            with self.subTest(total_cents=total_cents):
                self.assertEqual(loyalty_points(total_cents), expected)


class RefundTest(unittest.TestCase):
    def test_partial_refund(self):
        self.assertEqual(refund(1000, 250), 750)

    def test_full_refund(self):
        self.assertEqual(refund(1000, 1000), 0)

    def test_zero_refund(self):
        self.assertEqual(refund(1000, 0), 1000)
        self.assertEqual(refund(0, 0), 0)

    def test_rejects_invalid_amounts(self):
        for paid_cents, refund_cents in [
            (1000, 1500),
            (1000, -100),
            (0, 1),
            (-100, 0),
            (-100, -100),
            (-100, 100),
        ]:
            with self.subTest(paid_cents=paid_cents, refund_cents=refund_cents):
                with self.assertRaises(ValueError):
                    refund(paid_cents, refund_cents)


if __name__ == "__main__":
    unittest.main()
