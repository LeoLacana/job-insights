from src.sorting import sort_by
import pytest

jobs = [
    {'max_salary': 8000, 'min_salary': 1200, 'date_posted': '2022-01-01'},
    {'max_salary': 4300, 'min_salary': 1800, 'date_posted': '2021-02-02'},
    {'max_salary': 5200, 'min_salary': 2300, 'date_posted': '2021-09-09'},
    {'max_salary': 3300, 'min_salary': 1300, 'date_posted': '2019-12-12'},
    {'max_salary': 2900, 'min_salary': 1050, 'date_posted': '2020-07-07'},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == [
        {'max_salary': 2900, 'min_salary': 1050, 'date_posted': '2020-07-07'},
        {'max_salary': 8000, 'min_salary': 1200, 'date_posted': '2022-01-01'},
        {'max_salary': 3300, 'min_salary': 1300, 'date_posted': '2019-12-12'},
        {'max_salary': 4300, 'min_salary': 1800, 'date_posted': '2021-02-02'},
        {'max_salary': 5200, 'min_salary': 2300, 'date_posted': '2021-09-09'},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {'max_salary': 8000, 'min_salary': 1200, 'date_posted': '2022-01-01'},
        {'max_salary': 5200, 'min_salary': 2300, 'date_posted': '2021-09-09'},
        {'max_salary': 4300, 'min_salary': 1800, 'date_posted': '2021-02-02'},
        {'max_salary': 3300, 'min_salary': 1300, 'date_posted': '2019-12-12'},
        {'max_salary': 2900, 'min_salary': 1050, 'date_posted': '2020-07-07'},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {'max_salary': 8000, 'min_salary': 1200, 'date_posted': '2022-01-01'},
        {'max_salary': 5200, 'min_salary': 2300, 'date_posted': '2021-09-09'},
        {'max_salary': 4300, 'min_salary': 1800, 'date_posted': '2021-02-02'},
        {'max_salary': 2900, 'min_salary': 1050, 'date_posted': '2020-07-07'},
        {'max_salary': 3300, 'min_salary': 1300, 'date_posted': '2019-12-12'},
    ]

    with pytest.raises(TypeError):
        sort_by(jobs, "invalid", "second_invalid")
