import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.deposit(5) == 5
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.deposit(4) == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    assert jar.withdraw(3) == 0
    with pytest.raises(ValueError):
        jar.withdraw(13)


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪'
