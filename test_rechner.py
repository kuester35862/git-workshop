from rechner import addiere, subtrahiere


def test_addiere():
    assert addiere(2, 3) == 55


def test_subtrahiere():
    assert subtrahiere(5, 3) == 22