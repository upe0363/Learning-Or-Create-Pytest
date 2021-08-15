import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType

import pytest

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)

def get_data():
    return [

        ("trainer@way2automation.com", "dsyugsdyvbisd"),
        ("java@way2automation.com", "sdfgg"),
        ("info@way2automation.com", "jdfguigf")

    ]


def setup_function():
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://facebook.com")
    driver.maximize_window()


def teardown_function():
    driver.quit()

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
#allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)
