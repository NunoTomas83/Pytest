import pytest

from stuff.list_primes import *


@pytest.mark.prime
def test_is_prime():
    assert is_prime(3) is True


@pytest.mark.prime
def test_is_not_prime():
    assert is_prime(8) is False

@pytest.mark.prime
def test_list_of_primes():
    assert get_primes(9) == [2, 3, 5, 7]

