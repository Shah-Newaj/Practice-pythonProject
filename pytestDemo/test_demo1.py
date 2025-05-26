# any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
# pytest -v -s .\pytestDemo\test_demo1.py use this command to run the file
# pytest -v -s -k creditcard (run with regular expression for specific method)
# method name should have sense
# -k stands for method name execution, -s logs in output, -v stands for more info metadata
# you can mark (tag) test @pytest.mark.smoke and then run with -m => pytest -v -s -m smoke
# you can skip any test or method using @pytest.mark.skip
# run but will not document in the report @pytest.mark.xfail
# datadriven and parameterization can be done with return statements in tuple formats


import pytest

@pytest.mark.xfail
def test_firsProgram():
    print("Hello")

@pytest.mark.smoke
def test_greetcreditcard(setup):
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    # print(crossBrowser[0])
    print(crossBrowser[1])