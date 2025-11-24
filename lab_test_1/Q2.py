def calc(a, b):
    c = a + b
    d = a * b
    return c, d
def calculate_sum_and_product(a: int, b: int) -> tuple:
    """
    Calculate the sum and product of two numbers.

    Parameters:
        a (int): The first input number.
        b (int): The second input number.

    Returns:
        tuple: A tuple containing:
            - sum (int): a + b
            - product (int): a * b

    Example:
        >>> calculate_sum_and_product(3, 4)
        (7, 12)
    """
    total = a + b
    product = a * b
    return total, product


# testing
print(calculate_sum_and_product(5, 6))
