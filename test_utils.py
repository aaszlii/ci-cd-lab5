import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5)])
def test_add(a, b, expected):
    assert utils.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(5, 2, 3), (3, 3, 0)])
def test_subtract(a, b, expected):
    assert utils.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (4, 5, 20)])
def test_multiply(a, b, expected):
    assert utils.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(4, 2, 2.0), (10, 4, 2.5)])
def test_divide(a, b, expected):
    assert utils.divide(a, b) == expected


# TESTY DLA FUNKCJI BINARNEJ
@pytest.mark.parametrize(
    "n, expected", [(0, "0"), (1, "1"), (5, "101"), (100, "1100100")]
)
def test_to_binary_valid(n, expected):
    assert utils.to_binary(n) == expected


@pytest.mark.parametrize("n", [-1, 101])
def test_to_binary_out_of_range(n):
    with pytest.raises(ValueError):
        utils.to_binary(n)


@pytest.mark.parametrize("n", [1.5, "text", None])
def test_to_binary_invalid_type(n):
    with pytest.raises(ValueError):
        utils.to_binary(n)
