"""Prime Factor kata implementation."""


def prime_factors(number):
    """Return the prime factors of a positive integer in ascending order."""
    if isinstance(number, bool) or not isinstance(number, int) or number < 1:
        raise ValueError("number must be a positive integer")

    factors = []
    divisor = 2
    remaining = number

    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor += 1

    if remaining > 1:
        factors.append(remaining)

    return factors