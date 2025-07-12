from seasons import minutes
from datetime import date
import calendar
import pytest


def test_right_minutes():

    now = date.today()
    last_year = now.replace(year=now.year-1).isoformat()

    if calendar.isleap(now.year):
        assert minutes(last_year) == 527040
    else:
        assert minutes(last_year) == 525600


def test_raises():
    with pytest.raises(ValueError):
        minutes("three/four")
