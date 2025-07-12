import pytest

from fuel import (convert, gauge)


def test_convert():
    assert convert('0/100') <= 1
    assert convert('1/100') <= 1
    assert convert('100/100') >= 99
    assert convert('99/100') >= 99


def test_reprompt():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("3/5.5")
    with pytest.raises(ValueError):
        convert("5-10")
    with pytest.raises(ZeroDivisionError):
        convert('100/0')


def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'
    assert gauge(75) == '75%'
    assert gauge(25) == '25%'
