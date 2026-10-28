def apply_discount(price_cents: int, percent: int) -> int:
    """Return the price after a percentage discount, rounded down to whole cents."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return price_cents * (100 - percent) // 100


def total(items: list[int]) -> int:
    """Sum item prices in cents."""
    return sum(items)


def total_with_tax(items: list[int], tax_percent: int = 8) -> int:
    """Sum item prices plus tax, rounded down to whole cents."""
    subtotal = total(items)
    return subtotal + subtotal * tax_percent // 100


def total_with_shipping(items: list[int], shipping_cents: int = 500) -> int:
    """Sum item prices plus flat shipping, in cents."""
    return total(items) + shipping_cents


def apply_coupon(price_cents: int, code: str) -> int:
    """Apply a coupon code to a price in cents; raise ValueError for unknown codes."""
    if code == "SAVE10":
        return apply_discount(price_cents, 10)
    if code == "SAVE20":
        return apply_discount(price_cents, 20)
    raise ValueError(f"Unknown coupon code: {code}")


def loyalty_points(total_cents: int) -> int:
    """Loyalty points earned for an order: one point per whole dollar spent."""
    return total_cents // 10


def refund(paid_cents: int, refund_cents: int) -> int:
    """Return the amount still kept after refunding part of a payment, in cents."""
    return paid_cents - refund_cents
