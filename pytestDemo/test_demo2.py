# any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
# pytest -v -s .\pytestDemo\test_demo2.py use this command to run the file
# you can skip any method using @pytest.mark.skip

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_assertion():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_creditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"