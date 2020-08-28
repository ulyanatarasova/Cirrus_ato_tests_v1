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

class Section(Collection_test):
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.editor_selector = "//div[@role='textbox']"
        self.section_options = "//a[text()='Options']"
        self.section_questions = "//a[text()='Questions']"
        self.add_qustions = "//button[@class='rs_preserve toolbarButtonSkinAdjustment button-0-46 button-1Mv2-']"
        self.check_box_choose_all = "//label[@data-qa='table-check-all']"
        self.buttons_in_questions_modal_window = "//span[@class='footer-action-xyJxH']"
        self.add_time_in_field = "//input[@class='input-36b7z input-2b3GI']"
        self.checkboxes_on_options_tab = "//label[@class='label-2aRVS']"
        self.show_advanced_options = "//button[text()='Show advanced options']"
        self.checkboxes_on_options_tab_click_again = "//label[@class='label-2aRVS checked undefined']"

    def section_default(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section without questions', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.save_and_close_button(browser)

    def section_and_1_resource_file(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and 1 resource file', browser)

        self.add_resource_media_file_click(0, browser)

        self.select_picture('.pdf', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.save_and_close_button(browser)

    def section_and_1_media_file(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and 1 media file', browser)

        self.add_resource_media_file_click(1, browser)

        self.select_picture('.png', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.save_and_close_button(browser)

    def section_check_with_tax(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section with tax', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.taxonomy(varibles['taxonomy_1'], browser)

        self.save_and_close_button(browser)

    def section_check_with_lo(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.learning_objectives(varibles['learning objectives_1'], browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section with lo', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.save_and_close_button(browser)

    def section_check_item_purpose_formative(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section. Formative', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.select_item_purpose_formative(0, browser)

        self.save_and_close_button(browser)

    def section_check_item_purpose_summative(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section. Summative', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.select_item_purpose_summative(0, browser)

        self.save_and_close_button(browser)

    def section_check_disabled_options(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and check options are disabled', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.check_for_disabled("//input[@type='text']", browser)

        self.save_and_close_button(browser)

    def section_check_add_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and add in questions tab', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(0, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(2, self.buttons_in_questions_modal_window, 'click', 2, browser)

        self.save_and_close_button(browser)

    def section_check_add_and_close_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and add_and_close in questions tab',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions,'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0 , browser)

        self.save_and_close_button(browser)

    def section_check_options_tab_add_time_1(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and add_and_close in questions tab',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.add_time_in_field, 'send', '1', browser)

        self.save_and_close_button(browser)

    def section_check_options_tab_add_time_501(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and time more then 500',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.add_time_in_field, 'send', '501', browser)

        self.check_text_in_options_section(browser)

    def section_check_options_tab_add_time_0(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section with time 0',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.add_time_in_field, 'send', '0', browser)

        self.check_text_in_options_section(browser)

    def section_checkbox_show_section_introduction_page(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section + checkbox shown section introduction '
                                                                     'page',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.checkboxes_on_options_tab, 'click', 0, browser)

        self.save_and_close_button(browser)

    def section_checkbox_hide_detailed_information(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section + checkbox hide detailed information',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.checkboxes_on_options_tab, 'click', 0, browser)

        self.any_selector(0, "//div[@class='paper-2Mt3Y paper-33Xqj']", 'click', 0, browser)

        self.checkbox2_on_options_in_section(1, browser)

        self.save_and_close_button(browser)

    def section_all_checkboxes_avd_click_show_advanced_options(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section + all checkbox + click show advanced',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.checkboxes_on_options_tab, 'click', 0, browser)

        self.any_selector(0, "//div[@class='paper-2Mt3Y paper-33Xqj']", 'click', 0, browser)

        self.checkbox2_on_options_in_section(1, browser)

        self.any_selector(0, self.show_advanced_options, 'click', 0, browser)

        self.save_and_close_button(browser)

    def section_all_checkboxes_avd_pass_mark_50(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section + all checkbox + pass mark 50',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.checkboxes_on_options_tab, 'click', 0, browser)

        self.any_selector(0, "//div[@class='paper-2Mt3Y paper-33Xqj']", 'click', 0, browser)

        self.checkbox2_on_options_in_section(1, browser)

        self.any_selector(0, self.show_advanced_options, 'click', 0, browser)

        self.any_selector(1, self.add_time_in_field, 'send', '50', browser)

        self.save_and_close_button(browser)

    def section_all_checkboxes_and_number_of_questions_1(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section + all checkbox + number of questions',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.checkboxes_on_options_tab, 'click', 0, browser)

        self.any_selector(0, "//div[@class='paper-2Mt3Y paper-33Xqj']", 'click', 0, browser)

        self.checkbox2_on_options_in_section(1, browser)

        self.any_selector(0, self.show_advanced_options, 'click', 0, browser)

        self.select_value(browser)

        self.save_and_close_button(browser)

    def section_all_time_1_and_number_of_questions_1(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section + time 1 + number of questions',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.add_time_in_field, 'send', '1', browser)

        self.any_selector(0, self.show_advanced_options, 'click', 0, browser)

        self.select_value(browser)

        self.save_and_close_button(browser)

    def section_checkboxes_and_click_shown_int_after_hide(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section + shown intr page after hide',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions, 'click', 0, browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.buttons_in_questions_modal_window, 'click', 0, browser)

        self.any_selector(0, self.section_options, 'click', 0, browser)

        self.any_selector(0, self.checkboxes_on_options_tab, 'click', 0, browser)

        self.any_selector(0, "//div[@class='paper-2Mt3Y paper-33Xqj']", 'click', 0, browser)

        self.checkbox2_on_options_in_section(1, browser)

        self.any_selector(0, self.checkboxes_on_options_tab_click_again, 'click', 0, browser)

        self.save_and_close_button(browser)

    def section_check_alert_for_title(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.save_button(browser)

        self.check_alert_in_section(browser)

    def section_check_alert_for_section_text(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and check alert in section text', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.save_button(browser)

        self.check_alert_in_section(browser)

    def section_check_alert_for_introduction_text(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and check in introduction text', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.save_button(browser)

        self.check_alert_in_section(browser)

    def section_check_modal_window_after_click_cancel_click_yes(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and click cancel > yes without saving',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.cancel_button(browser)

        self.warning_after_click_cancel_yes(0, browser)

    def section_check_modal_window_after_click_cancel_click_cancel(self, varibles, browser):
        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and click cancel > cancel without saving',
                          browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.cancel_button(browser)

        self.warning_after_click_cancel_cancel(0, browser)










