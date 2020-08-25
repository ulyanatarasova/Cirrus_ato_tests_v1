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

    elif domen_name == "cirrusplatform":
        print("\nstart cirrusplatform for test..")
        domen = "https://test-education.cirrusplatform.com/"

    else:
        raise pytest.UsageError("--domen_name should be ....")
    return domen

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def varibles():
    variables = {
        'user':{
            'login':'ulyana',
            'password':['u', 'l', 'y', 'a', 'n', 'a']
        },
        'collection_name': 'Collection Regression',
        'score_1':'1',
        'score_2':'2',
        'score_3':'3',

        'question_mc': {
        'title': 'MC'},

        'question_emc': {
        'title': 'EMC'},

        'question_mr': {
            'title': 'MR',
        },

        'question_either_or': {
            'title': 'Either_or',
        },

        'question_numeric_specific': {
            'title': 'Numeric_specific',
        },

        'question_numeric_range': {
            'title': 'Numeric_range',
        },

        'question_SFL': {
            'title': 'SFL',
        },

        'question_fill_blank': {
            'title': 'FITB',
        },

        'question_order': {
            'title': 'Order',
        },

        'question_Match': {
            'title': 'Match',
        },

        'question_Hotspot': {
            'title': 'Hotspot',
        },

        'question_extended_match': {
            'title': 'Extended match',
        },

        'question_drag_and_drop': {
            'title': 'Drag and drop',
        },

        'question_comprehensive_integrated_puzzle': {
            'title': 'CIP',
        },

        'question_financial_statement': {
            'title': 'Financial_statement',
        },

        'question_programming': {
            'title': 'Programming',
        },

        'question_mathematical': {
            'title': 'Mathematical',
        },

        'question_short_answer': {
            'title': 'Short answer',
        },

        'question_essay': {
            'title': 'Essay',
        },

        'question_file_response': {
            'title': 'File response',
        },

        'question_section': {
            'title': 'Section',
        },

        'question_page_welcome': {
            'title': 'Welcome',
        },

        'question_page_finish': {
            'title': 'Finish',
        },

        'question_page_other': {
            'title': 'Other',
        }
    }
    return variables