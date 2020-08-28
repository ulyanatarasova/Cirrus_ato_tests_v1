import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os.path
from random import choice
from string import ascii_letters
from string import digits
from .body_of_mc_tests import MC



@pytest.mark.main
def test_creating_collection(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.creating_collection(varibles, browser)

@pytest.mark.main
def test_mc_default(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_default(varibles, browser)

@pytest.mark.main
def test_mc_add_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_add_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_add_alternatives_remove(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_add_alternatives_remove(varibles, browser)

@pytest.mark.main
def test_mc_dont_add_radio_button(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_dont_add_radio_button(varibles, browser)

@pytest.mark.main
def test_mc_add_alternatives_remove_dont_add_radio_button(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_add_alternatives_remove_dont_add_radio_button(varibles, browser)

@pytest.mark.main
def test_mc_and_1_resource_file(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_and_1_resource_file(varibles, browser)

@pytest.mark.main
def test_mc_and_1_media_file(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_and_1_media_file(varibles, browser)

@pytest.mark.main
def test_mc_check_with_tax(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_with_tax(varibles, browser)

@pytest.mark.main
def test_mc_check_with_lo(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_with_lo(varibles, browser)

@pytest.mark.main
def test_mc_check_item_purpose_formative(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_item_purpose_formative(varibles, browser)

@pytest.mark.main
def test_mc_check_item_purpose_summative(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_item_purpose_summative(varibles, browser)

@pytest.mark.main
def test_mc_check_seed(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_seed(varibles, browser)

@pytest.mark.main
def test_mc_click_options(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_click_options(varibles, browser)

@pytest.mark.main
def test_mc_options_click_detailed_feedback(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_detailed_feedback(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_general_show_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_general_show_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_general_show_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_general_show_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_general_show_on_questions_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_general_show_on_questions_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_detailed_show_on_questions_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_detailed_show_on_questions_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_detailed_show_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_detailed_show_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_detailed_show_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_detailed_show_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_general_randomize_options(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_general_randomize_options(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_general_randomize_options_fixed_position(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_general_randomize_options_fixed_position(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_detailed_randomize_options(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_detailed_randomize_options(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_detailed_randomize_options_fixed_position(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_detailed_randomize_options_fixed_position(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_general_randomize_options_fixed_position_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_general_randomize_options_fixed_position_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_options_click_feedback_general_randomize_options_fixed_position_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_options_click_feedback_general_randomize_options_fixed_position_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_feedback_general_randomize_options_fixed_position_on_questions_and_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_feedback_general_randomize_options_fixed_position_on_questions_and_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_detailed_randomize_options_fixed_position_on_questions_and_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_randomize_options_fixed_position_on_questions_and_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_detailed_randomize_options_fixed_position_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_randomize_options_fixed_position_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_detailed_randomize_options_fixed_position_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_randomize_options_fixed_position_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_detailed_randomize_options_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_randomize_options_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_detailed_randomize_options_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_randomize_options_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_general_randomize_options_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_general_randomize_options_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_general_randomize_options_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_general_randomize_options_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_general_add_labels(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_general_add_labels(varibles, browser)

@pytest.mark.main
def test_mc_detailed_add_labels(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_add_labels(varibles, browser)

@pytest.mark.main
def test_mc_general_add_labels_show_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_general_add_labels_show_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_general_add_labels_show_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_general_add_labels_show_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_general_add_labels_show_on_alternatives_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_general_add_labels_show_on_alternatives_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_detailed_add_labels_show_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_add_labels_show_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_detailed_add_labels_show_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_add_labels_show_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_detailed_add_labels_show_on_alternatives_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_detailed_add_labels_show_on_alternatives_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_workout_general(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_workout_general(varibles, browser)

@pytest.mark.main
def test_mc_workout_detailed(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_workout_detailed(varibles, browser)

@pytest.mark.main
def test_mc_workout_general_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_workout_general_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_workout_detailed_on_alternatives(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_workout_detailed_on_alternatives(varibles, browser)

@pytest.mark.main
def test_mc_workout_general_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_workout_general_on_questions(varibles, browser)

@pytest.mark.test
def test_mc_workout_detailed_on_questions(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_workout_detailed_on_questions(varibles, browser)

@pytest.mark.main
def test_mc_check_alert_for_title(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_alert_for_title(varibles, browser)

@pytest.mark.main
def test_mc_check_modal_window_after_click_cancel_click_yes(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_modal_window_after_click_cancel_click_yes(varibles, browser)

@pytest.mark.main
def test_mc_check_modal_window_after_click_cancel_click_cancel(domen, browser, varibles):
    object = MC(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mc_check_modal_window_after_click_cancel_click_cancel(varibles, browser)