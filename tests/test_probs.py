import pytest

from nbc import (
    trained,
    prob
)


@pytest.fixture()
def df():
    return trained()


def test_good_is_nice(df):
    result = prob('good', 'nice', df)
    assert result == 1.0


def test_john_is_fifty_fifty(df):
    result = prob('John', 'nice', df)
    assert result == 0.5
