from nbc import (
    trained,
    prob
)


def test_good_is_nice():
    df = trained()
    result = prob('good', 'nice', df)
    assert result == 1.0
