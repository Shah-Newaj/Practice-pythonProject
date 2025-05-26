#pytest -v -s .\pytestDemo\test_fixtureDemo.py
# fixture are used as setup and tear down methods for test cases
# conftest file used to generalize fixture and make it available to all test cases
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")

