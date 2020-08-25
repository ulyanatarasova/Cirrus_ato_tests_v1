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
        self.value_input = "//input[@class='input-36b7z']"
        self.add_blank_selector = "//a[@id='add-blank']"
        self.add_choice_selector = "//a[@id='add-choice']"
        self.section_options = "//a[text()='Options']"
        self.section_questions = "//a[text()='Questions']"
        self.add_qustions = "//button[@class='rs_preserve toolbarButtonSkinAdjustment button-0-46 button-1Mv2-']"
        self.check_box_choose_all = "//label[@data-qa='table-check-all']"
        self.add_and_close = "//span[@class='footer-action-xyJxH']"

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

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section with lo', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.learning_objectives(varibles['learning objectives_1'], browser)

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

    def section_check_with_questions(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(4)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and check options are disabled', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.any_selector(0, self.section_questions, 'click', 0, browser)

        self.any_selector(0, self.add_qustions,'click', 0,browser)

        time.sleep(1)

        self.any_selector(0, self.check_box_choose_all, 'click', 0, browser)

        self.any_selector(1, self.add_and_close, 'click', 0 , browser)

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

        self.check_alert(browser)

    def section_check_alert_for_section_text(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and check alert in section text', browser)

        self.any_selector(1, self.editor_selector, 'send', 'There is section introduction text in the field',
                          browser)

        self.save_button(browser)

        self.check_alert(browser)

    def section_check_alert_for_introduction_text(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section and check in introduction text', browser)

        self.any_selector(0, self.editor_selector, 'send', 'There is section text in the field', browser)

        self.save_button(browser)

        self.check_alert(browser)




