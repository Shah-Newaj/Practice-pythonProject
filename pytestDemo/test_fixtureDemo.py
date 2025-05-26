#pytest -v -s .\pytestDemo\test_fixtureDemo.py

import pytest

@pytest.fixture()
def setup():
    print("I will be executed first")

    yield
    print("I will be executed last")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
