#conftest file used to generalize fixture and make it available to all test cases

import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")

    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Shah", "Newaj", "Shuvro"]

@pytest.fixture(params=[("chrome", "Shah"), ("firefox", "Newaj"), ("edge", "Shuvro")])
def crossBrowser(request):
    return request.param
