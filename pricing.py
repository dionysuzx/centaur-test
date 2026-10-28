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
    """Apply a coupon code to a price in cents."""
    if code == "SAVE10":
        return apply_discount(price_cents, 10)
    if code == "SAVE20":
        return apply_discount(price_cents, 20)
    return price_cents
