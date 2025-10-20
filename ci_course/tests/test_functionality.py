import ci_course

def test_greet():
    """
    Test the function `greet` in functionality.py
    """
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"


def test_minimum():
    """
    Test the function `minimum` in functionality.py
    """
    assert ci_course.minimum(1, 2, 3) == 1
    assert ci_course.minimum(1.2, 2.3) == 1.2
    assert ci_course.minimum(-1.2, -3) == -3

def test_minimum_returns_none_for_non_numeric_args():
    """minimum() should return None when given only non-numeric arguments."""
    result = ci_course.minimum("a", "b", None)
    assert result is None
