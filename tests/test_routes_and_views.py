from pytest import fixture
from flask import Flask
from flask.testing import FlaskClient

from src.app import create_app

TOTAL_JOBS = 3323


@fixture(scope="session")
def app() -> Flask:
    return create_app()


@fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_index_view_status_200(client: FlaskClient):
    assert client.get("/").status_code == 200


def test_index_view_has_readme_content(client: FlaskClient):
    response = client.get("/")
    assert b"Boas vindas ao" in response.data
    assert b"projeto Job Insights" in response.data


def test_jobs_view_status_200(client: FlaskClient):
    assert client.get("/jobs").status_code == 200


def test_jobs_view_status_200_with_params(client: FlaskClient):
    query_params = [
        "amount=0",
        "amount=1",
        "amount=10",
        "amount=20000",
        "amount=",
        "amount=aloha",
        "first_job=0",
        "first_job=1",
        "first_job=10",
        "first_job=20000",
        "first_job=",
        "first_job=aloha",
        "salary=0",
        "salary=1",
        "salary=10",
        "salary=20000",
        "salary=",
        "salary=aloha",
        "industry=0",
        "industry=1",
        "industry=10",
        "industry=20000",
        "industry=",
        "industry=aloha",
        "job_type=0",
        "job_type=1",
        "job_type=10",
        "job_type=20000",
        "job_type=",
        "job_type=aloha",
    ]
    for param in query_params:
        assert client.get(f"/jobs?{param}").status_code == 200


def test_job_route_exists(app: Flask):
    assert any(
        rule.rule == "/job/<index>" for rule in app.url_map.iter_rules()
    )


def test_job_view_exists(app: Flask):
    from src.routes_and_views import job  # noqa
    import inspect

    args = inspect.getfullargspec(job)[0]
    assert len(args) == 1, 'Parameter "index" not found'
    assert args[0] == "index", 'Parameter "index" not found'


def test_job_view_status_200(client: FlaskClient):
    for job in range(TOTAL_JOBS):
        assert client.get(f"/job/{job}").status_code == 200


def test_job_view_has_job_information(client: FlaskClient):
    with open("tests/mocks/job_1.html") as file:
        assert file.read() == client.get("/job/1").get_data(as_text=True)
