from src.jobs import read


def test_read_jobs():
    results = read("src/jobs.csv")

    assert type(results) == list
    assert len(results) == 3324
    for result in results:
        assert type(result) == dict

    results = read("tests/mocks/jobs.csv")

    assert type(results) == list
    assert len(results) == 3
    expected_list = [
        {"title": "Front end developer", "salary": "2000", "type": "trainee"},
        {"title": "Back end developer", "salary": "3000", "type": "full time"},
        {
            "title": "Full stack end developer",
            "salary": "4000",
            "type": "full time",
        },
    ]
    for result, expected in zip(results, expected_list):
        assert result == expected
