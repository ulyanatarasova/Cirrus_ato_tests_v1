<<<<<<< HEAD
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--domen_name', action='store', default=None,
                     help="Choose domen")


@pytest.fixture(scope="function")
def domen(request):
    domen_name = request.config.getoption("domen_name")
    browser = None
    if domen_name == "cirrus0":
        print("\nstart cirrus0 for test..")
        domen = "https://test-education.cirrus0.eu/"

    elif domen_name == "cirrus1":
        print("\nstart cirrus1 for test..")
        domen = "https://test-education.cirrus1.eu/"

    elif domen_name == "cirrus2":
        print("\nstart cirrus2 for test..")
        domen = "https://test-education.cirrus2.eu/"

    elif domen_name == "cirrus3":
        print("\nstart cirrus3 for test..")
        domen = "https://test-education.cirrus3.eu/"

    elif domen_name == "cirrus4":
        print("\nstart cirrus4 for test..")
        domen = "https://test-education.cirrus4.eu/"

    elif domen_name == "cirrus5":
        print("\nstart cirrus5 for test..")
        domen = "https://test-education.cirrus5.eu/"

    else:
        raise pytest.UsageError("--domen_name should be ....")
    return domen

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
=======
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--domen_name', action='store', default=None,
                     help="Choose domen")


@pytest.fixture(scope="function")
def domen(request):
    domen_name = request.config.getoption("domen_name")
    browser = None
    if domen_name == "cirrus0":
        print("\nstart cirrus0 for test..")
        domen = "https://test-education.cirrus0.eu/"

    elif domen_name == "cirrus1":
        print("\nstart cirrus1 for test..")
        domen = "https://test-education.cirrus1.eu/"

    elif domen_name == "cirrus2":
        print("\nstart cirrus2 for test..")
        domen = "https://test-education.cirrus2.eu/"

    elif domen_name == "cirrus3":
        print("\nstart cirrus3 for test..")
        domen = "https://test-education.cirrus3.eu/"

    elif domen_name == "cirrus4":
        print("\nstart cirrus4 for test..")
        domen = "https://test-education.cirrus4.eu/"

    elif domen_name == "cirrus5":
        print("\nstart cirrus5 for test..")
        domen = "https://test-education.cirrus5.eu/"

    else:
        raise pytest.UsageError("--domen_name should be ....")
    return domen

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
>>>>>>> c14724a7421cd42b355bc801c3e0a0f9a2e263dd
    browser.quit()