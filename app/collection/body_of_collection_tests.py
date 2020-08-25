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


class Collection_test(Cirrus):
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.editor_selector = "//div[@role='textbox']"
        self.value_input = "//input[@class='input-36b7z']"
        self.add_blank_selector = "//a[@id='add-blank']"
        self.add_choice_selector = "//a[@id='add-choice']"
        self.programming_textarea = "//textarea[@class='ace_text-input']"
        self.programming_test_cases = "//a[text()='Test cases']"
        self.programming_execution_options = "//a[text()='Execution options']"
        self.math_solution_selector = "//textarea[@class='solution-attr']"
        self.programming_requested_files = "//a[text()='Requested files']"
        self.programming_create = "//button[text()='Create']"

    def question_multiple_choice_test(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Multiple choice', browser)

        for i in range(4):
            self.editor(i, None, 'mc', browser, varibles)

        self.radio_button(0, browser)

        self.score(varibles['score_2'], browser)

        self.save_and_close_button(browser)

    def question_emc(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Extended multiple choice', browser)

        #self.editor(0, None, 'emc', browser, varibles)

        self.scroll_win(0, 1000, browser)

        self.editor(4, 'click', 'emc', browser, varibles)

        for i in range(4, 6):
            self.editor(i, None, 'emc', browser, varibles)

        self.scroll_win(0, 1000, browser)

        self.scroll_win(0, -600, browser)

        self.data_qa_selector('click', 0, 'label', 'label-alternative_text_button', 0, browser)

        self.scroll_win(0, 600, browser)

        self.data_qa_selector('click', 0, 'label', 'label-alternative_text_button', 2, browser)

        self.score(varibles['score_3'], browser)

        self.save_and_close_button(browser)

    def question_mr(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(5)

        self.add_question(browser)

        self.choose_question('Multiple response', browser)

        for i in range(4):
            self.editor(i, None, 'mr', browser, varibles)

        self.check_box_click(0, browser)

        self.save_and_close_button(browser)

    def question_either_or(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Either/Or', browser)

        # settings of the question
        for i in range(3):
            self.editor(i, None, 'either_or', browser, varibles)

        self.radio_button(0, browser)

        self.save_and_close_button(browser)

    def question_numeric_specific(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Numeric', browser)

        self.any_selector(0, self.editor_selector, 'send', 'Numeric specific', browser)

        self.any_selector(3, self.value_input, 'send', '1', browser)

        self.save_and_close_button(browser)

    def question_numeric_range(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Numeric', browser)

        self.any_selector(0, self.editor_selector, 'send', 'Numeric range', browser)

        self.any_selector(1, "//div[@class='radio-1cQ4X']", 'click', 1, browser)

        for i in range(3, 5):
            self.any_selector(i, self.value_input , 'send', i, browser)


        self.save_and_close_button(browser)

    def question_SFL(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Select from list', browser)

        self.editor(1, None, 'SFL', browser, varibles)

        self.any_selector(1, self.editor_selector, 'send', u'\ue008' + u'\ue012' + u'\ue012', browser)

        self.any_selector(0, self.add_blank_selector, 'click', 0, browser)

        self.data_qa_selector('send', 'No', 'input', 'blanked-words', 0, browser)

        self.save_and_close_button(browser)

    def question_fill_blank(self, varibles, browser):
        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Fill in the blank', browser)

        self.editor(1, None, 'fill_blank', browser, varibles)

        self.any_selector(1, self.editor_selector, 'send', u'\ue008' + u'\ue012' + u'\ue012', browser)

        self.any_selector(0, self.add_blank_selector, 'click', 0, browser)

        self.data_qa_selector('send', 'No', 'input', 'blanked-words', 0, browser)

        self.save_and_close_button(browser)

    def question_order(self, varibles, browser):
        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Order', browser)

        for i in range(4):
            self.editor(i, None, 'order', browser, varibles)

        self.data_qa_selector('click', 0, 'a', 'add-alternative-button', 0, browser)

        time.sleep(3)
        self.editor(4, None, 'order', browser, varibles)

        self.save_and_close_button(browser)

    def question_Match(self, varibles, browser):
        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Match', browser)

        for i in range(7):
            self.editor(i, None, 'Match', browser, varibles)

        self.save_and_close_button(browser)

    def question_Hotspot(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Hotspot', browser)

        self.editor(0, None, 'Hotspot', browser, varibles)

        self.data_qa_selector('click', 0, 'button', 'add-file-button', 0, browser)

        self.select_picture('.png', browser)

        self.draw(browser)

        self.save_and_close_button(browser)

    def extended_match_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Extended match', browser)

        self.editor(0, None, 'extended_match', browser, varibles)

        self.any_selector(0, "//button[@id='qe-ext_match_mode']", 'click', 0, browser)

        for i in range(1, 5):
            self.editor(i, None, 'extended_match', browser, varibles)

        index = 12
        for i in range(2):
            self.circle(index, browser)
            index = index + 2

        index = 14
        for i in range(2):
            self.circle(index, browser)
            index = index + 2

        self.save_and_close_button(browser)

    def drag_and_drop_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Drag and drop', browser)

        self.any_selector(0, self.editor_selector, 'send', 'Drag and drop', browser)

        self.data_qa_selector('click', 0, 'button', 'add-file-button', 0, browser)

        self.select_picture('.png', browser)

        element = self.single_method(0, 'image', browser)

        self.move_element(element, 50, 50, browser)

        self.any_selector(0, self.add_choice_selector, 'click', 0, browser)

        self.data_qa_selector('click', 0, 'button', 'add-file-button', 0, browser)

        self.select_picture('.png', browser)

        self.scroll_win(0, 1500, browser)

        element = self.single_method(0, 'circle', browser)

        self.move_element(element, 200, 1, browser)

        self.save_and_close_button(browser)

    def comprehensive_integrated_puzzle_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Comprehensive Integrated Puzzle', browser)

        self.any_selector(0, self.editor_selector, 'send', 'Comprehensive Integrated Puzzle', browser)

        ipq = ['Column header', 'Row', 'Body']

        index = 0
        for i in range(4, 7):
            self.any_selector(i, "//input[@type='text']", 'send', ipq[index], browser)
            index = index + 1

        self.save_and_close_button(browser)

    def financial_statement_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Financial statement', browser)

        self.any_selector(0, self.editor_selector, 'send', 'Financial statement', browser)

        self.any_selector(0, "//input[@data-qa='fs-section-title']", 'send', 'Some header', browser)

        selector = ['fs-title', 'fs-title', 'fs-debit', 'fs-debit', 'fs-credit', 'fs-credit']
        text = ['First title', 'Second title', '1', '2', '1', '2']
        index = 0
        for i in range(len(selector)):
            if index == 2:
                index = 0
            self.any_selector(index, f"//input[@data-qa='{selector[i]}']", 'send', text[i], browser)
            index = index + 1

        self.save_and_close_button(browser)

    def programming_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Programming', browser)

        self.any_selector(0, self.editor_selector, 'send', 'Programming', browser)

        self.any_selector(0, self.programming_test_cases, 'click', 1, browser)

        self.any_selector(0, self.programming_textarea, 'send',
                                                                             "case = Test 7+5\n"
                                                                            "input = 5 \n"
                                                                            "7 \n"
                                                                            "output = 12 \n"
                                                                            "\n"
                                                                            "case = Test 10+18 \n"
                                                                            "input = 10 \n"
                                                                            "18 \n"
                                                                            "output = 28 \n"
                                                                            "\n"
                                                                            "case = Test 13+(-17) \n"
                                                                            "input = 13 \n"
                                                                            "-17 \n"
                                                                            "output = -4 \n"
                                                                            "\n"
                                                                            "case = Test 1024+1024 \n"
                                                                            "input = 1024 \n"
                                                                            "1024 \n"
                                                                            "output = 2048", browser)

        self.any_selector(0, self.programming_execution_options, 'click', 2, browser)

        index = 0
        for i in range(2):
            self.any_selector(index, "//option[@value='1']",  'click', 0, browser)
            index = index + 2

        self.any_selector(0, self.programming_requested_files, 'click', 0, browser)

        self.any_selector(0, self.programming_create, 'click', 0, browser)

        self.any_selector(0, "//input[@value='']", 'send', 'index.js', browser)

        self.any_selector(0, "//button[@class='reset-2Sxmr button-2DTz8 rs_preserve filled-success-19y_v "
                             "filledSuccess-0-4']",
                          'click', 0, browser)

        self.any_selector(0, self.programming_textarea, 'send', "const readline = "
                                                                            "require('readline');\n"
                                                                            "const sum = (num1,num2) => {\n"
                                                                            "    //This function should return"
                                                                            " sum of values\n"
                                                                            "return null;\n"
                                                                            "};\n"
                                                                            "\n"
                                                                            "const rl = readline.createInterface({\n"
                                                                            "  input: process.stdin,\n"
                                                                            "  output: process.stdout\n"
                                                                            "});\n"
                                                                            "var num1 = null;\n"
                                                                            "var num2 = null;\n"
                                                                            "\n"
                                                                            "rl.question('', (var1) => {\n"
                                                                            "    rl.question('', "
                                                                            "(var2) => {\n"
                                                                            "        var num1 = parseInt(var1);\n"
                                                                            "        var num2 = parseInt(var2);\n"
                                                                            "        console.log(sum(num1, num2));\n"
                                                                            "        rl.close();\n"
                                                                            "    });\n"
                                                                            "});", browser)

        self.save_and_close_button(browser)

    def mathematical_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Mathematical question', browser)

        self.any_selector(0, self.editor_selector,'send', 'Mathematical question_1', browser)

        self.any_selector(0, self.math_solution_selector, 'send', '1', browser)

        self.any_selector(0, "//button[@data-qa='question-editor-actions-save']", 'click', 0, browser)

        self.any_selector(0, "//div[@class='alert alert-success alert-dismissible']" ,'click', 0, browser)

        self.any_selector(0, "//a[@data-section='questionSet']", 'click', 0, browser)

        self.any_selector(0, "//button[@data-qa='sowiso-set-add']",'click', 0, browser)

        self.any_selector(0, self.editor_selector, 'send', 'Mathematical question_2', browser)

        self.any_selector(0, self.math_solution_selector, 'send', '2', browser)

        self.save_and_close_button(browser)

    def short_answer_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Short answer', browser)

        self.any_selector(0, "//div[@role='textbox']", 'send', 'Short answer', browser)

        self.any_selector(0, "//input[@class='qe-sa-alt_text border']", 'send', '1', browser)

        self.save_and_close_button(browser)

    def essay_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Essay', browser)

        self.any_selector(0, "//div[@role='textbox']", 'send', 'Essay', browser)

        self.save_and_close_button(browser)

    def file_response_question(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('File response', browser)

        self.any_selector(0, "//div[@role='textbox']", 'send', 'file_response', browser)

        self.save_and_close_button(browser)

    def section(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Section', browser)

        self.any_selector(0, "//input[@id='questionTitle']", 'send', 'Section', browser)

        self.any_selector(0, "//div[@role='textbox']", 'send', 'There is section text in the field', browser)

        self.any_selector(1, "//div[@role='textbox']", 'send', 'There is section introduction text in the field',
                          browser)

        self.save_and_close_button(browser)

    def page_welcome(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Page', browser)

        self.any_selector(0, "//input[@class='form-control']", 'send', 'Welcome page', browser)

        self.any_selector(0, "//div[@role='textbox']", 'send', 'Some text', browser)

        self.save_and_close_button(browser)

    def page_finish(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Page', browser)

        self.any_selector(0, "//input[@class='form-control']", 'send', 'Finish page', browser)

        self.any_selector(0, "//div[@role='textbox']", 'send', 'Some text', browser)

        self.any_selector(0, "//option[@value='2']", 'click', 0, browser)

        self.save_and_close_button(browser)

    def page_other(self, varibles, browser):

        self.search(varibles['collection_name'], browser)

        time.sleep(2)

        self.add_question(browser)

        self.choose_question('Page', browser)

        self.any_selector(0, "//input[@class='form-control']", 'send', 'Other page', browser)

        self.any_selector(0, "//div[@role='textbox']", 'send', 'Some text', browser)

        self.any_selector(0, "//option[@value='3']", 'click', 0, browser)

        self.save_and_close_button(browser)

    #def change_status_to_live(self, browser):
    #    alert = WebDriverWait(browser, 10).until(
    #        EC.element_to_be_clickable((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
    #    alert.click()
    #    # alert_off = WebDriverWait(browser, 10).until_not(
    #    # EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
    #
    #    # self.browser.find_element_by_xpath("//span[@aria-hidden='true']").click()
    #    select_all = WebDriverWait(browser, 10).until(
    #        EC.element_to_be_clickable((By.XPATH, "//label[@data-qa='table-check-all']")))
    #   select_all.click()
    #    action = browser.find_element_by_xpath("//button[@data-qa='collection-actions']")
    #    action.click()
    #   change_status = browser.find_element_by_xpath("//div[text()='Change status']")
    #    change_status.click()
    #    browser.find_element_by_xpath("//div[@data-qa='submenu-change-status-draft']")
    #    live = browser.find_element_by_xpath("//div[@data-qa='submenu-change-status-live']")
    #    live.click()
    #    confim_button = browser.find_element_by_xpath("//span[text()='Yes']")
    #    confim_button.click()

