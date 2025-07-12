from numb3rs import validate


def test_ip_numbers():
    assert validate('127.1.1.1') == True
    assert validate('127.0.0.1') == True
    assert validate('0.0.0.0') == True


def test_invalid():
    assert validate('cat') == False
    assert validate('256.255.255.255') == False
    assert validate('64.128.256.512') == False
    assert validate('127.1.1.1.') == False
    assert validate('1a7.1.1.1') == False
    assert validate('10.10.10.10.10') == False
    assert validate('10.10.10') == False
    assert validate('64.128.256.512') == False
    assert validate('2001:0db8:85a3:0000:0000:8a2e:0370:7334') == False
