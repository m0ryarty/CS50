from um import count


def test_ums():
    assert count('um,') == 1
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2
    assert count('1, um, two um, 3 um, many ums') == 3


def test_no_ums():
    assert count('Yummy') == 0
    assert count('my umbrella!') == 0
