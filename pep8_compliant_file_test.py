# Tests for basic arithmetic operations and a greeting message.


def test_calc_addition():
    """Test du résultat de 2 + 4."""
    output = 2 + 4
    assert output == 6


def test_calc_subtraction():
    """Test du résultat de 2 - 4."""
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    """Test du résultat de 2 * 4."""
    output = 2 * 4
    assert output == 8


def test_coucou():
    """Test si le résultat renvoie 'hello'."""
    output = "hello"
    assert output == "hello"
