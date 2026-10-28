def apply_discount(price_cents: int, percent: int) -> int:
    """Return the price after a percentage discount, rounded down to whole cents."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return price_cents * percent // 100


def total(items: list[int]) -> int:
    """Sum item prices in cents."""
    return sum(items)


def total_with_shipping(items: list[int], shipping_cents: int = 500) -> int:
    """Sum item prices plus flat shipping, in cents."""
    return total(items) + shipping_cents
