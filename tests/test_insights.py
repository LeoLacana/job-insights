import pytest
from src.insights import (
    get_unique_job_types,
    filter_by_job_type,
    get_unique_industries,
    filter_by_industry,
    get_max_salary,
    get_min_salary,
    matches_salary_range,
    filter_by_salary_range,
)

JOB_TYPES = {
    "PART_TIME": {"jobs": 172},
    "OTHER": {"jobs": 39},
    "FULL_TIME": {"jobs": 3078},
    "CONTRACTOR": {"jobs": 14},
    "TEMPORARY": {"jobs": 2},
    "INTERN": {"jobs": 19},
}
INDUSTRIES = {
    "Health Care": {"jobs": 232},
    "Arts, Entertainment & Recreation": {"jobs": 2},
    "Biotech & Pharmaceuticals": {"jobs": 317},
    "Agriculture & Forestry": {"jobs": 1},
    "Consumer Services": {"jobs": 7},
    "Accounting & Legal": {"jobs": 29},
    "Insurance": {"jobs": 29},
    "Restaurants, Bars & Food Services": {"jobs": 3},
    "Non-Profit": {"jobs": 10},
    "Transportation & Logistics": {"jobs": 8},
    "Business Services": {"jobs": 583},
    "Retail": {"jobs": 63},
    "Aerospace & Defense": {"jobs": 144},
    "Construction, Repair & Maintenance": {"jobs": 66},
    "Media": {"jobs": 29},
    "Real Estate": {"jobs": 5},
    "Finance": {"jobs": 223},
    "Information Technology": {"jobs": 679},
    "Education": {"jobs": 60},
    "Telecommunications": {"jobs": 35},
    "Manufacturing": {"jobs": 42},
    "Government": {"jobs": 105},
    "Oil, Gas, Energy & Utilities": {"jobs": 28},
}
UNINFORMED_INDUSTRIES = 624
TOTAL_JOBS = 3324
TOTAL_JOBS_WITH_SPECIFIED_SALARY = 2232
MAX_SALARY = 383416
MIN_SALARY = 19857


def test_total_jobs_in_job_types():
    assert TOTAL_JOBS == sum([type_["jobs"] for type_ in JOB_TYPES.values()])


def test_total_jobs_in_industries():
    assert TOTAL_JOBS - UNINFORMED_INDUSTRIES == sum(
        [industry["jobs"] for industry in INDUSTRIES.values()]
    )


def test_get_unique_job_types():
    result = get_unique_job_types("src/jobs.csv")
    assert len(result) == 6

    for type_ in JOB_TYPES.keys():
        assert type_ in result

    result = get_unique_job_types("tests/mocks/jobs_with_types.csv")
    assert len(result) == 2
    assert "full time" in result
    assert "trainee" in result


@pytest.fixture()
def jobs_for_filter_by_job_type():
    return [
        {"id": 1, "job_type": "PART_TIME"},
        {"id": 2, "job_type": "PART_TIME"},
        {"id": 3, "job_type": "OTHER"},
        {"id": 4, "job_type": "OTHER"},
        {"id": 5, "job_type": "FULL_TIME"},
        {"id": 6, "job_type": "FULL_TIME"},
        {"id": 7, "job_type": "CONTRACTOR"},
        {"id": 8, "job_type": "CONTRACTOR"},
        {"id": 9, "job_type": "TEMPORARY"},
        {"id": 10, "job_type": "TEMPORARY"},
        {"id": 11, "job_type": "INTERN"},
        {"id": 12, "job_type": "INTERN"},
    ]


def test_filter_by_job_type(jobs_for_filter_by_job_type):
    types = [
        "PART_TIME",
        "OTHER",
        "FULL_TIME",
        "CONTRACTOR",
        "TEMPORARY",
        "INTERN",
    ]
    id_ = 1
    for type_ in types:
        jobs = filter_by_job_type(jobs_for_filter_by_job_type, type_)
        assert len(jobs) == 2
        assert jobs[0]["id"] == id_
        assert jobs[1]["id"] == id_ + 1
        id_ += 2
    jobs = filter_by_job_type(jobs_for_filter_by_job_type, "")
    assert len(jobs) == 0


def test_get_unique_industries():
    result = get_unique_industries("src/jobs.csv")

    assert len(result) == len(INDUSTRIES)

    for industry in INDUSTRIES:
        assert industry in result

    # * Mock
    result = get_unique_industries("tests/mocks/jobs_with_industries.csv")
    assert len(result) == 2
    assert "agriculture" in result
    assert "solar energy" in result


@pytest.fixture()
def jobs_for_filter_by_industry():
    return [
        {"id": 1, "industry": "agriculture"},
        {"id": 2, "industry": "agriculture"},
        {"id": 3, "industry": "solar energy"},
        {"id": 4, "industry": "solar energy"},
        {"id": 5, "industry": "bank"},
        {"id": 6, "industry": "bank"},
        {"id": 7, "industry": "mechanical engineering"},
        {"id": 8, "industry": "mechanical engineering"},
        {"id": 9, "industry": "translation"},
        {"id": 10, "industry": "translation"},
        {"id": 11, "industry": "finances"},
        {"id": 12, "industry": "finances"},
    ]


def test_filter_by_industries(jobs_for_filter_by_industry):
    industries = [
        "agriculture",
        "solar energy",
        "bank",
        "mechanical engineering",
        "translation",
        "finances",
    ]
    id_ = 1
    for industry in industries:
        jobs = filter_by_industry(jobs_for_filter_by_industry, industry)
        assert len(jobs) == 2
        assert jobs[0]["id"] == id_
        assert jobs[1]["id"] == id_ + 1
        id_ += 2
    jobs = filter_by_industry(jobs_for_filter_by_industry, "")
    assert len(jobs) == 0


def test_get_max_salary():
    assert get_max_salary("src/jobs.csv") == MAX_SALARY
    assert get_max_salary("tests/mocks/jobs_with_salaries.csv") == 8000


def test_get_min_salary():
    assert get_min_salary("src/jobs.csv") == MIN_SALARY
    assert get_min_salary("tests/mocks/jobs_with_salaries.csv") == 1000


def test_matches_salary_range():
    invalid_jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": -1, "min_salary": 10},
    ]
    jobs = [
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 1500, "min_salary": 0},
    ]
    salaries = [0, 1, 5, 1000, 2000, -1, -2]
    expected = [
        [False, False, False, True, True, False, False],
        [True, True, True, True, False, False, False],
    ]

    for job in invalid_jobs:
        for salary in salaries:
            with pytest.raises(ValueError):
                matches_salary_range(job, salary)

    for job_index in range(len(jobs)):
        for salary_index in range(len(salaries)):
            result = matches_salary_range(
                jobs[job_index], salaries[salary_index]
            )
            assert result == expected[job_index][salary_index]

    invalid_types = [None, "", [], {}, lambda: 1]
    for invalid in invalid_types:
        with pytest.raises(ValueError):
            matches_salary_range(
                {"max_salary": "1000", "min_salary": invalid}, 20
            )
        with pytest.raises(ValueError):
            matches_salary_range(
                {"min_salary": "1000", "max_salary": invalid}, 20
            )
        with pytest.raises(ValueError):
            matches_salary_range(
                {"min_salary": "100", "max_salary": "1000"}, invalid
            )
    with pytest.raises(ValueError):
        matches_salary_range({"max_salary": "1000"}, 10)
    with pytest.raises(ValueError):
        matches_salary_range({"min_salary": "1000"}, 10)


def test_filter_by_salary_range():
    jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": -1, "min_salary": 10},
    ]
    salaries = [0, 1, 5, 1000, 2000, -1, -2, None, "", [], {}, lambda: 1]
    expected = [
        [jobs[3], jobs[4]],  # 0
        [jobs[3], jobs[4]],  # 1
        [jobs[3], jobs[4]],  # 5
        [jobs[2], jobs[3], jobs[4]],  # 1000
        [jobs[2], jobs[3]],  # 2000
        [],  # -1
        [],  # -2
        [],  # None
        [],  # ""
        [],  # []
        [],  # {}
        [],  # lambda: 1
    ]
    for salary_index in range(len(salaries)):
        assert (
            filter_by_salary_range(jobs, salaries[salary_index])
            == expected[salary_index]
        )
