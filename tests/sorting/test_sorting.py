# from src.sorting import sort_by
from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    jobs = [
        {"max_salary": 30},
        {"max_salary": 20},
        {"max_salary": 10},
        {"max_salary": 5},
        {"max_salary": ""},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"max_salary": 30},
        {"max_salary": 20},
        {"max_salary": 10},
        {"max_salary": 5},
        {"max_salary": ""},
    ]
