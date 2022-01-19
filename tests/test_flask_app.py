from pytest import fixture
from flask import Flask
from flask.testing import FlaskClient

from src.app import create_app


@fixture
def client() -> FlaskClient:
    return create_app().test_client()


def test_create_app_returns_flask_instance(client):
    assert type(create_app()) == Flask
