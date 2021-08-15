import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_markereport(item, call):
    outcome = yield
    rep = outcome.got_reult()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):

    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if request.param == "firefox":
        driver = webdriver.firefox

    driver.get("http://facebook.com")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
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
def test_dologin(username, password, get_browser):
    driver = get_browser
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
# allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)
