import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os.path
from random import choice
from string import ascii_letters
from string import digits
from .body_of_section_tests import Section



@pytest.mark.main
def test_creating_collection(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.creating_collection(varibles, browser)

@pytest.mark.main
def test_section_default(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_default(varibles, browser)

@pytest.mark.main
def test_section_and_1_resource_file(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_and_1_resource_file(varibles, browser)

@pytest.mark.main
def test_section_and_1_media_file(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_and_1_media_file(varibles, browser)

@pytest.mark.main
def test_section_check_with_tax(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_with_tax(varibles, browser)

@pytest.mark.main
def test_section_check_with_lo(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_with_lo(varibles, browser)

@pytest.mark.main
def test_section_check_item_purpose_formative(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_item_purpose_formative(varibles, browser)

@pytest.mark.main
def test_section_check_item_purpose_summative(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_item_purpose_summative(varibles, browser)

@pytest.mark.main
def test_section_check_disabled_options(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_disabled_options(varibles, browser)


@pytest.mark.main
def test_question_multiple_choice(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_multiple_choice_test(varibles, browser)
    #object.question_multiple_choice_test(varibles, browser) + add queston


@pytest.mark.test
def test_section_check_with_question(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_with_questions(varibles, browser)

@pytest.mark.main
def test_section_check_alert_for_title(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_alert_for_title(varibles, browser)

@pytest.mark.main
def test_section_check_alert_for_section_text(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_alert_for_section_text(varibles, browser)

@pytest.mark.main
def test_section_check_alert_for_introduction_text(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_alert_for_introduction_text(varibles, browser)