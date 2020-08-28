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

@pytest.mark.test
def test_add_questions_to_section(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_multiple_choice_test(varibles, browser)
    #object.question_multiple_choice_test(varibles, browser) + add queston

@pytest.mark.main
def test_section_check_add_questions(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_add_questions(varibles, browser)

@pytest.mark.main
def test_section_check_add_and_close_questions(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_add_and_close_questions(varibles, browser)

@pytest.mark.main
def test_section_check_options_tab_add_time_1(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_options_tab_add_time_1(varibles, browser)

@pytest.mark.main
def test_section_check_options_tab_add_time_501(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_options_tab_add_time_501(varibles, browser)

@pytest.mark.main
def test_section_check_options_tab_add_time_0(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_options_tab_add_time_0(varibles, browser)

@pytest.mark.main
def test_section_checkbox_show_section_introduction_page(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_checkbox_show_section_introduction_page(varibles, browser)

@pytest.mark.main
def test_section_checkbox_hide_detailed_information(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_checkbox_hide_detailed_information(varibles, browser)

@pytest.mark.main
def test_section_all_checkboxes_avd_click_show_advanced_options(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_all_checkboxes_avd_click_show_advanced_options(varibles, browser)

@pytest.mark.main
def test_section_all_checkboxes_avd_pass_mark_50(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_all_checkboxes_avd_pass_mark_50(varibles, browser)

@pytest.mark.main
def test_section_all_checkboxes_and_number_of_questions_1(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_all_checkboxes_and_number_of_questions_1(varibles, browser)

@pytest.mark.test
def test_section_all_time_1_and_number_of_questions_1(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_all_time_1_and_number_of_questions_1(varibles, browser)

@pytest.mark.main
def test_section_checkboxes_and_click_shown_int_after_hide(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_checkboxes_and_click_shown_int_after_hide(varibles, browser)

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

@pytest.mark.main
def test_section_check_modal_window_after_click_cancel_click_yes(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_modal_window_after_click_cancel_click_yes(varibles, browser)

@pytest.mark.main
def test_section_check_modal_window_after_click_cancel_click_cancel(domen, browser, varibles):
    object = Section(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section_check_modal_window_after_click_cancel_click_cancel(varibles, browser)