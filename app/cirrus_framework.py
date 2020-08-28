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



class Cirrus:
    def search(self, collection_name, browser):

        open_tab_collection = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='infobox_block cmn-block-margin']")))
        open_tab_collection.click()

        collection_list = browser.find_elements_by_xpath("//div[@class='listViewItem__column ']")

        collection = browser.find_elements_by_xpath("//div[@data-qa='collections-list-item']")

        index = 0
        for i in collection_list:

            current_collection = collection_list[index].__getattribute__('text')

            if current_collection == collection_name:
                collection[index].click()

                break
            index = index + 1

    def login(self, domen, browser):
        try:
           browser.get(domen)
           browser.implicitly_wait(10)

           login_link = browser.find_element_by_xpath("//a[@href='#']")
           login_link.click()
           login_item_username = browser.find_element_by_xpath("//input[@id='login']")
           login_item_username.send_keys(self.username)
           login_item_password = browser.find_element_by_xpath("//input[@id='view_password']")

           for i in range(len(self.username)):
              login_item_password.send_keys(self.password[i])

           login_button = browser.find_element_by_xpath("//button[@class='btn btn-green-filled submitButton']")
           login_button.click()
           login_author = browser.find_element_by_xpath("//a[@href='author/app']")
           login_author.click()
        except:
            self.login(domen, browser)

    def creating_collection(self, varibles, browser):

        open_tab_collection = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='infobox_block cmn-block-margin']")))
        open_tab_collection.click()

        time.sleep(5)

        add_collection = browser.find_element_by_xpath("//a[@class='btn btn-tlbr btn-tlbr-green']")
        add_collection.click()

        title_of_collection = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@data-qa='collection-title-input']")))
        title_of_collection.send_keys(varibles['collection_name'])

        confim_button_collection = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(
            (By.XPATH, ("//button[@class='reset-2Sxmr button-2DTz8 rs_preserve filled-success-19y_v "
                        "filledSuccess-0-4']"))))
        confim_button_collection.click()

        alert = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
        alert.click()

    def save_and_close_button(self, browser):
        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

        alert = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//button["
                                                                                            "@id='add-menu']")))
        alert.click()

    def add_question(self, browser):
        add_question = WebDriverWait(browser, 2000).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                            "@id='add-menu']")))
        add_question.click()

    def choose_question(self, question_name, browser):
        choose_type_of_question = browser.find_element_by_xpath(f"//a[text()='{question_name}']")
        choose_type_of_question.click()

    def check_box_click(self, index, browser):
        browser.find_elements_by_xpath("//label[@class='label-2aRVS']")[index].click()

    def radio_button(self, index, browser):
        browser.find_elements_by_xpath("//label[@class='']")[index].click()

    def scroll_win(self, scroll_from, scroll_to, browser):
        browser.execute_script(f"window.scrollBy({scroll_from}, {scroll_to});")

    def data_qa_selector(self, action, text, selector_tag, selector_atr, index, browser):
        if action is 'click':
            browser.find_elements_by_xpath(f"//{selector_tag}[@data-qa='{selector_atr}']")[index].click()
        elif action is 'send':
            browser.find_elements_by_xpath(f"//{selector_tag}[@data-qa='{selector_atr}']")[index].send_keys(text)

    def any_selector(self, index, selector, action, text, browser):
        if action is 'click':
            send_value = browser.find_elements_by_xpath(selector)
            send_value[index].click()

        elif action is 'send':

            send_value = browser.find_elements_by_xpath(selector)
            send_value[index].send_keys(text)

    def add_aternatives(self, browser):
        browser.find_element_by_xpath("//button[@class='reset-2Sxmr button-2DTz8 rs_preserve success-1JvQB success-0-2"
                                       " c0149']").click()

    def add_aternatives_remove(self, index, browser):
        browser.find_elements_by_xpath("//i[@class='icon icon-cross']")[index].click()

    def select_picture(self, expansion, browser):
        all_items = browser.find_elements_by_xpath("//div[@class='listViewItem__column']")
        for element in all_items:
            if expansion in element.text:
                time.sleep(1.5)
                browser.find_element_by_xpath(f"//div[text()='{element.text}']").click()
                break

    def draw(self, browser):
        time.sleep(2)
        browser.find_element_by_xpath("//label[@data-action='ellipse']").click()

        element = browser.find_element_by_tag_name("image")

        action = ActionChains(browser)
        hov = action.drag_and_drop_by_offset(element, 20, 20).perform()

        hov_2 = action.drag_and_drop_by_offset(element, 100, 0).perform()

    def editor(self, index, action, question_name, browser, varibles):
        if action is None:
                time.sleep(1)
                browser.find_elements_by_xpath("//div[@role='textbox']")[index].send_keys(varibles[f'question'
                                                                                               f'_{question_name}'][
                                                                                          'title']+str(index))
        elif action is "click":
            open_field_1 = browser.find_elements_by_xpath("//div[@class='editorContainer-20GnD "
                                                          "editorContainerActive-c96i1']")
            for i in range(index):
                open_field_1[i].click()
                time.sleep(1)
                browser.find_elements_by_xpath("//div[@role='textbox']")[i].send_keys(varibles[f'question'
                                                                                            f'_{question_name}'][
                                                                                          'title']+str(i))

    def circle(self, index, browser):
        browser.find_elements_by_tag_name("circle")[index].click()
        time.sleep(1)

    def move_element(self, element, x, y, browser):
        time.sleep(1)
        action = ActionChains(browser)
        hov = action.drag_and_drop_by_offset(element, x, y).perform()

    def single_method(self, index, selector, browser):
        element = browser.find_elements_by_tag_name(selector)[index]
        return element

    def score(self, text, browser):
        score_input = browser.find_element_by_xpath("//input[@class='input-36b7z' and @value='1']")
        score_input.send_keys(u'\ue003' + text)

    def add_resource_media_file_click(self, index, browser):
        browser.find_elements_by_xpath("//div[@class='facadeL-2Y1JS iconLayout-Tjtdo']")[index].click()

    def select_item_purpose_formative(self, index, browser):
        browser.find_elements_by_xpath("//label[@data-qa='label-qe-item-purpose-formative-button']")[index].click()

    def select_item_purpose_summative(self, index, browser):
        browser.find_elements_by_xpath("//label[@data-qa='label-qe-item-purpose-summative-button']")[index].click()

    def select_seed_yes(self, index, browser):
        browser.find_elements_by_xpath("//label[@data-qa='label-qe-seedItem-yes-button']")[index].click()

    def taxonomy(self, value, browser):
        select = browser.find_element_by_xpath("//select[@data-qa='qe-taxonomies-select']")
        select.click()
        option = browser.find_element_by_xpath(f"//option[text()='{value}']")
        option.click()

    def learning_objectives(self, value, browser):
        lo_button = browser.find_element_by_xpath("//button[@data-qa='qe-lo-add-button']")
        lo_button.click()

        select = browser.find_element_by_xpath("//select[@data-qa='select-objective-repository']")
        select.click()

        option = browser.find_element_by_xpath(f"//option[text()='{value}']")
        option.click()

        time.sleep(1)
        checkbox = browser.find_element_by_xpath("//label[@class='checkbox-inline']")
        checkbox.click()
        time.sleep(1)
        ok_button = browser.find_element_by_xpath("//button[@data-qa='ok-button']")
        ok_button.click()

    def check_for_disabled(self, selector, browser):
        disabled = browser.find_element_by_xpath(selector)
        assert disabled.is_enabled() == False, "Error. Options should be disabled."

    def save_button(self, browser):
        save_button = browser.find_element_by_xpath("//button[@data-qa='question-editor-actions-save']")
        save_button.click()

    def cancel_button(self, browser):
        cancel_button = browser.find_element_by_xpath("//button[@data-qa='question-editor-actions-cancel']")
        cancel_button.click()

    def warning_after_click_cancel_yes(self, index, browser):
        browser.find_elements_by_xpath("//button[@data-qa='dialog-confirm-button']")[index].click()

    def warning_after_click_cancel_cancel(self, index, browser):
        browser.find_elements_by_xpath("//button[@data-qa='dialog-cancel-button']")[index].click()

    def check_alert_in_section(self, browser):
        try:
          alert = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                     "//div[@class='c0166']")))
        except:
            raise ValueError("Error. Alert was not found.")

    def check_alert_in_questions(self, browser):
        try:
          alert = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "//div[@class='c011']")))
        except:
            raise ValueError("Error. Alert was not found.")

    def check_text_in_options_section(self, browser):
        try:
          text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Please"
                                                                            " enter a value between 1 and 500']")))
        except:
            raise ValueError("Error. Alert was not found.")

    def checkbox2_on_options_in_section(self, index, browser):
        hide = browser.find_elements_by_xpath("//div[@class='checkbox-3v829']")[index]
        hide.click()

    def click_options_in_question_editor(self, browser):
        browser.find_element_by_xpath("//button[@data-qa='control-link']").click()

    def click_detailed_feedback(self, browser):
        for i in browser.find_elements_by_xpath("//label[@class='']"):
            try:
                i.click()
            except:
                pass

    def select_value(self, browser):
        select = browser.find_elements_by_tag_name('select')
        select[1].click()
        select[1].send_keys(u'\ue015' + u'\ue007')

    def question_editor_options_advanced_options_checkboxes(self, index, browser):
        alternatives = browser.find_elements_by_xpath("//label[@class='label-2aRVS']")[index]
        alternatives.click()





