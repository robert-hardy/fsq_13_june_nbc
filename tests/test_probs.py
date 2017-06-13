from nbc import (
    trained,
    prob
)


def test_good_is_nice():
    df = trained()
    result = prob('good', 'nice', df)
    assert result == 1.0


def test_john_is_fifty_fifty():
    df = trained()
    result = prob('John', 'nice', df)
    assert result == 0.5
