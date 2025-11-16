def add(a: float, b: float) -> float:
    """Return the sum of two numeric values.

    Accepts integers or floats. Raises a TypeError if either argument
    is not numeric.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("add() expects numeric arguments (int or float)")
    return a + b
