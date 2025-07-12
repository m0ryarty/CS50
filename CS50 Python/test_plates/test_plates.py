from plates import is_valid


def test_lenght():
    assert is_valid('aaa1234') == False
    assert is_valid('a') == False
    assert is_valid('aaa123') == True


def test_first_letters():
    assert is_valid('50CS') == False
    assert is_valid('5CS0') == False


def test_number_place():
    assert is_valid('aaa12a') == False
    assert is_valid('aa0') == False
    assert is_valid('aaa0') == False
    assert is_valid('aaaa0') == False
    assert is_valid('aaaaa0') == False


def test_no_ponctuation():
    assert is_valid('PI3.14') == False


def test_only_letters():
    assert is_valid('aaaaaa') == True
    assert is_valid('123456') == False
