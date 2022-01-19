from unittest.mock import patch
import pytest
from tests.sorting import mocks
from src.sorting import sort_by


def strict_xfail(mocked, expected=AssertionError):
    """
    Sets up parametrization with a mocked implementation expected to fail.

    Parameters
    ----------
    mocked : function
        the mocked implementation to try out.
    expected : Exception, optional
        An expected Exception, by default AssertionError

    Returns
    -------
    pytest.param
        Configured param for pytest fixture parametrization.
    """
    return pytest.param(
        mocked, marks=pytest.mark.xfail(raises=expected, strict=True)
    )


mocking = [
    strict_xfail(mocks.sort_by_strings),
    strict_xfail(mocks.sort_by_descending),
    strict_xfail(mocks.sort_by_any_criteria),
    sort_by,
]


@pytest.fixture(autouse=True, params=mocking)
def mock_it(request):
    with patch("test_sorting.sort_by", request.param):
        yield
