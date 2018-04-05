"""Math functions for calculator."""


def add(lst):
    """Return the sum of the two inputs."""

    return lst[0] + lst[1]


def subtract(lst):
    """Return the second number subtracted from the first."""

    return lst[0] - lst[1]


def multiply(lst):
    """Multiply the two inputs together."""

    return lst[0] * lst[1]


def divide(lst):
    """Divide the first input by the second and return the result."""

    return lst[0] / lst[1]


def square(lst):
    """Return the square of the input."""

    return lst[0] ** 2


def cube(lst):
    """Return the cube of the input."""

    return lst[0] ** 3


def power(lst):
    """Raise lst to the power o and return the value."""

    return lst[0] ** lst[1]


def mod(lst):
    """Return the remainder of lst ."""

    return lst[0] % lst[1]


def add_mult(lst):
    """Returns sum of lst an, multiplied by num3"""

    return add(lst) * lst[2]


def add_cubes(lst):
    """Cubes lst an and returns the sum"""

    return (lst[0] ** 3) + (lst[1] ** 3)
    