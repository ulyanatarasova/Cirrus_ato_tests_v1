import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import os.path

from random import choice
from string import ascii_letters
from string import digits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from app.cirrus_framework import Cirrus
from ..collection.body_of_collection_tests import Collection_test

class MC(Collection_test):
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.editor_selector = "//div[@role='textbox']"
        self.section_options = "//a[text()='Options']"
        self.section_questions = "//a[text()='Questions']"
        self.add_qustions = "//button[@class='rs_preserve toolbarButtonSkinAdjustment button-0-46 button-1Mv2-']"
        self.check_box_choose_all = "//label[@data-qa='table-check-all']"
        self.buttons_in_questions_modal_window = "//span[@class='footer-action-xyJxH']"

    def mc_default(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_add_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.add_aternatives(browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_add_alternatives_remove(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.add_aternatives(browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.add_aternatives_remove(0, browser)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_dont_add_radio_button(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.save_button(browser)

        self.check_alert_in_questions(browser)

    def mc_add_alternatives_remove_dont_add_radio_button(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.add_aternatives(browser)

        self.radio_button(0, browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.add_aternatives_remove(0, browser)

        self.save_button(browser)

        self.check_alert_in_questions(browser)

    def mc_and_1_resource_file(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.add_resource_media_file_click(0, browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_and_1_media_file(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.add_resource_media_file_click(1, browser)

        self.select_picture('.png', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_check_with_tax(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.taxonomy(varibles['taxonomy_1'], browser)

        self.save_and_close_button(browser)

    def mc_check_with_lo(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.learning_objectives(varibles['learning objectives_1'], browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_check_item_purpose_formative(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.select_item_purpose_formative(0, browser)

        self.save_and_close_button(browser)

    def mc_check_item_purpose_summative(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.select_item_purpose_summative(0, browser)

        self.save_and_close_button(browser)

    def mc_check_seed(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.select_seed_yes(0, browser)

        self.save_and_close_button(browser)

    def mc_click_options(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_detailed_feedback(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_general_show_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_general_show_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.click_options_in_question_editor(browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_general_show_on_questions_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.click_options_in_question_editor(browser)

        for i in range(8):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_detailed_show_on_questions_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.click_detailed_feedback(browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.click_options_in_question_editor(browser)

        for i in range(10):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_detailed_show_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.click_detailed_feedback(browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_detailed_show_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.click_detailed_feedback(browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_general_randomize_options(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_general_randomize_options_fixed_position(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_detailed_randomize_options(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_detailed_randomize_options_fixed_position(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_general_randomize_options_fixed_position_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_options_click_feedback_general_randomize_options_fixed_position_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_options_in_question_editor(browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_feedback_general_randomize_options_fixed_position_on_questions_and_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_options_in_question_editor(browser)

        for i in range(8):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_randomize_options_fixed_position_on_questions_and_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(10):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_randomize_options_fixed_position_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_randomize_options_fixed_position_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_randomize_options_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_randomize_options_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_general_randomize_options_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_general_randomize_options_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.click_options_in_question_editor(browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_general_add_labels(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_add_labels(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_general_add_labels_show_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_general_add_labels_show_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_options_in_question_editor(browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_general_add_labels_show_on_alternatives_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_options_in_question_editor(browser)

        for i in range(8):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_add_labels_show_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_add_labels_show_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_detailed_add_labels_show_on_alternatives_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(1, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.question_editor_options_advanced_options_checkboxes(0, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(10):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_workout_general(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(4, browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_workout_detailed(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(4, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_workout_general_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_workout_detailed_on_alternatives(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(2, browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_workout_general_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.click_options_in_question_editor(browser)

        for i in range(5):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_workout_detailed_on_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.click_options_in_question_editor(browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.question_editor_options_advanced_options_checkboxes(3, browser)

        self.click_detailed_feedback(browser)

        self.click_options_in_question_editor(browser)

        for i in range(7):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def mc_check_alert_for_title(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        self.any_selector(1, self.editor_selector, 'send', 'question1', browser)

        self.any_selector(2, self.editor_selector, 'send', 'question2',
                          browser)

        self.any_selector(3, self.editor_selector, 'send', 'question3',
                          browser)

        self.radio_button(0, browser)

        self.save_button(browser)

        self.check_alert_in_questions(browser)

    def mc_check_modal_window_after_click_cancel_click_yes(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.cancel_button(browser)

        self.warning_after_click_cancel_yes(0, browser)

    def mc_check_modal_window_after_click_cancel_click_cancel(self, varibles, browser):
        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.cancel_button(browser)

        self.warning_after_click_cancel_cancel(0, browser)










