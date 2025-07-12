from working import convert
import pytest


def test_am():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') != '9:00 to 17:00'
    assert convert('9:00 PM to 5:00 AM') == '21:00 to 05:00'
    assert convert('12:00 PM to 12:00 AM') == '12:00 to 00:00'


def test_minute():
    assert convert('9:35 AM to 5:45 PM') == '09:35 to 17:45'
    assert convert('9:35 PM to 5:45 AM') == '21:35 to 05:45'


def test_no_minute():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert convert('9 PM to 5 AM') == '21:00 to 05:00'


def test_raises():
    with pytest.raises(ValueError):
        convert('hello')
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:00 PM')
    with pytest.raises(ValueError):
        convert('9:00 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('9:00 AM to 15:00 PM')
    with pytest.raises(ValueError):
        convert('13:00 AM to 5:00 PM')
