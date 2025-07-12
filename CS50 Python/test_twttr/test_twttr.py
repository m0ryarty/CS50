from twttr import shorten


def test_a():
    assert shorten('arara') == 'rr'


def test_e():
    assert shorten('emende') == 'mnd'


def test_i():
    assert shorten('vitimi') == 'vtm'


def test_o():
    assert shorten('coco') == 'cc'


def test_u():
    assert shorten('urubu') == 'rb'


def test_A():
    assert shorten('ARARA') == 'RR'


def test_E():
    assert shorten('EMENDE') == 'MND'


def test_I():
    assert shorten('VITIMI') == 'VTM'


def test_O():
    assert shorten('COCO') == 'CC'


def test_U():
    assert shorten('URUBU') == 'RB'


def test_number():
    assert shorten('CS50') == 'CS50'


def test_punctuation():
    assert shorten('CS50.!?:;') == 'CS50.!?:;'
