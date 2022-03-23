def test_bool():
    assert True


def test_int():
    assert 3 != 4


def test_str():
    assert "ex" in "example"


def test_type():
    assert isinstance(21, int)
