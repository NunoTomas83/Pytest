# Multiplication test ideas

# 2 positive ints
# identity: multiplying any number by 1
# zero:  multiplying any number by 0
# positive by negative
# negative by negative
# multiply floats


# a parametrized test function

import pytest

products = [
    (2, 3, 6),              # positive ints
    (1, 99, 99),            # identity
    (0, 3, 0),              # zero
    (4, -3, -12),            # positive by negative
    (-5, -5, 25),           # negative by negativa
    (2.5, 6.7, 16.75),      # floats
]


@pytest.mark.math
@pytest.mark.parametrize("a, b, product", products)
def test_multi(a, b, product):
    assert a * b == product


