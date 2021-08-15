import pytest


@pytest.mark.sanity
def testlogin():
    print("login Successful")


def testlogoff():
    print("logoff Successful")


@pytest.mark.sanity
def testcalculation():
    assert 2 + 4 == 6
