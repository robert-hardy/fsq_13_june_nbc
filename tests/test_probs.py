import pytest

from nbc import (
    trained_stacked,
    docprob,
    prob
)


@pytest.fixture()
def df():
    return trained_stacked()


def test_good_is_nice(df):
    result = prob('good', 'nice', df)
    assert result == 1.0


def test_john_is_fifty_fifty(df):
    result = prob('John', 'nice', df)
    assert result == 0.5


def test_foo_is_fifty_fifty(df):
    result = prob('foo', 'nice', df)
    assert result == 0.5

def test_cat_is_fifty_fifty(df):
    result = prob('cat', 'nice', df)
    assert result == 0.5


def test_doc_is_good(df):
    result = docprob('John is good', 'nice', df)
    assert result == 1.0
