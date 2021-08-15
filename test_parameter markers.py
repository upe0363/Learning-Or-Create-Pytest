import pytest


def get_data():

    return[

        ("trainer@way2automation.com","dsyugsdyvbisd"),
        ("java@way2automation.com", "sdfgg"),
        ("info@way2automation.com", "jdfguigf")

    ]

@pytest.mark.parametrize("username,password",get_data())
def test_dologin(username,password):
    print(username,"-----",password)


