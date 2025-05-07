"""Module containing basic calculator functions."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the division of a by b."""
    return a / b

def to_binary(n):
    """Convert natural number [0–100] to binary string."""
    if not isinstance(n, int) or n < 0 or n > 100:
        raise ValueError("Input must be a natural number between 0 and 100.")
    return bin(n)[2:]
