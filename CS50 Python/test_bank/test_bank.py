from bank import value


def test_hello():
    assert value('hello') == 0
    assert value('how are you') == 20
    assert value('what') == 100
    assert value('hey') == 20
    assert value('Hello') == 0
    assert value('How are you') == 20
    assert value('What') == 100
    assert value('Hey') == 20
