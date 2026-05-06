from rechner import addiere, subtrahiere


def test_addiere():
    assert addiere(2, 3) == 5


def test_subtrahiere():
    assert subtrahiere(5, 3) == 2