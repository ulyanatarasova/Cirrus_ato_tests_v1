import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import os.path

import pyautogui as root

from random import choice
from string import ascii_letters
from string import digits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains





class Collection_test():
    browser = webdriver.Chrome()
    password = ['1','2','3','4','5']
    username ='un1'
    link = "https://test-education.cirrus0.eu/"

    def registration(self):
        self.browser.get(self.link)
        self.browser.implicitly_wait(10)
        # login in sistem
        login_link = self.browser.find_element_by_xpath("//a[@href='#']")
        login_link.click()
        login_item_username = self.browser.find_element_by_xpath("//input[@id='login']")
        login_item_username.send_keys(self.username)
        login_item_password = self.browser.find_element_by_xpath("//input[@id='view_password']")
        login_item_password.send_keys(self.password[0])
        login_item_password.send_keys(self.password[1])
        login_item_password.send_keys(self.password[2])
        login_item_password.send_keys(self.password[3])
        login_item_password.send_keys(self.password[4])
        login_button = self.browser.find_element_by_xpath("//button[@class='btn btn-green-filled submitButton']")
        login_button.click()
        login_author = self.browser.find_element_by_xpath("//a[@href='author/app']")
        login_author.click()

    def assessment_test(self):
        try:
             self.registration()
             # creating an assesment
             assesment = self.browser.find_element_by_xpath("//div[@data-href='#assessments/overview']")
             assesment.click()
             add_assesment = self.browser.find_element_by_xpath("//a[@data-qa='assessments-add']")
             add_assesment.click()
             #option_radio = WebDriverWait(self.browser, 5).until(
                #EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='label-formative']")))
             #option_radio.click()

             option_radio1 = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='label-mixed']")))
             option_radio1.click()
             option_radio1 = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH, "//label[@data-qa='label-mixed']")))
             option_radio1.click()
             #option_checkbox = self.browser.find_element_by_xpath("//label[@data-qa='print']")
             #option_checkbox.click()
             assesment_title = self.browser.find_element_by_xpath("//input[@data-qa='assessment-title']")
             assesment_title.send_keys('Fixed Assessment')
             assesment_code = self.browser.find_element_by_xpath("//input[@data-qa='assessment-code']")
             assesment_code.send_keys('Fixed Assessment')
             assesment_confim = self.browser.find_element_by_xpath("//button[@data-qa='new-assessment-save']")
             assesment_confim.click()
             # settings of the assesment
             assesment_code = self.browser.find_element_by_xpath("//input[@id='ExternalId']")
             Id = (''.join(choice(ascii_letters + digits) for i in range(7)))
             assesment_code.send_keys(Id)
             save_externalId = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='assessment-i-save']")))
             save_externalId.click()

             alert=WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//button[@class='close']")))
             alert.click()
             #alert = WebDriverWait(browser, 5).until_not(
               #EC.invisibility_of_element_located((By.XPATH, "//div[class()='alert alert-success alert-dismissible']")))
             time.sleep(2)
             go_to_options = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//div[text()='options']")))

             go_to_options.click()
             self.browser.find_elements_by_tag_name("select")[2].click()
             self.browser.find_element_by_xpath("//option[text()='After each attempt']").click()
             #time.sleep(5)
             check_box = self.browser.find_element_by_xpath("//label[@data-qa='assessment-options-show-only-status']")
             check_box.click()
             self.browser.execute_script("window.scrollBy(0, 800);")
             save_options = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//span[text()='Save']")))
             save_options.click()
             #time.sleep(3)
             self.browser.execute_script("window.scrollBy(0, -1200);")
             alert = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//button[@class='close']")))
             alert.click()
             go_to_selection = self.browser.find_element_by_xpath("//div[text()='question selection']")
             go_to_selection.click()

             #-------------------------------------------------------------------------------------------------------
             time.sleep(2)
             side_bar = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//i[@class='fa fa-bars']")))
             side_bar.click()

             list_of_all_items = []
             all_items = self.browser.find_elements_by_xpath("//span[@class='lbl']")
             for element in all_items:
                 list_of_all_items.append(element.text)

             list_of_png_pictures = []
             for element in list_of_all_items:
                 if 'Collection Regression' in element:
                     list_of_png_pictures.append(element)
                 else:
                     print("Not satisfy collection")

             print(list_of_png_pictures)
             choose_collection_by_text=self.browser.find_element_by_xpath(f"//span[text()='"
                                                                          f"{list_of_png_pictures[0]}']")
             choose_collection_by_text.click()
             #-------------------------------------------------------------------------------------------------------
             select_question =  WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='table-check-all']")))
             select_question.click()
             #time.sleep(5)
             adding_question = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='manual-selection-add-questions']")))
             adding_question.click()
             #time.sleep(5)
             forms = self.browser.find_element_by_xpath("//div[text()='forms']")
             forms.click()

             adding_form = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//button[@class='rs_preserve toolbarButtonSkinAdjustment button-0-1 button-1Mv2-']")))
             adding_form.click()
             adding_fixed_form = self.browser.find_element_by_xpath("//label[@data-qa='label-gen-form-fixed']")
             adding_fixed_form.click()
             creating_form = self.browser.find_element_by_xpath("//button[@data-qa='assessment-gf-save']")
             creating_form.click()
             forms_settings = self.browser.find_element_by_xpath("//div[text()='Form A']")
             forms_settings.click()
             #time.sleep(1)
             self.browser.find_elements_by_xpath("//button[@data-qa='']")[0].click()
             first_choice = self.browser.find_element_by_xpath("//div[@data-qa='1']")
             first_choice.click()
             self.browser.find_elements_by_xpath("//div[@class='div-12z2j td-2Bgor cell-in-sorted-row-Rxf0B "
                                             "column-3JUVA']")[0].click()
             self.browser.find_elements_by_xpath("//button[@data-qa='']")[1].click()
             second_choice = self.browser.find_element_by_xpath("//div[@data-qa='2']")
             second_choice.click()
             self.browser.find_elements_by_xpath("//div[@class='div-12z2j td-2Bgor cell-in-sorted-row-Rxf0B "
                                             "column-3JUVA']")[1].click()
             self.browser.execute_script("window.scrollBy(0, -500);")
             going_to_options = self.browser.find_element_by_xpath("//a[text()='Options']")
             going_to_options.click()
             #time.sleep(2)
             assesment_scale = self.browser.find_element_by_xpath("//div[@class='easCombobox-2aPdw "
                                                               "assessmentScales-24XfV rs_preserve']")
             assesment_scale.click()
             passed_notpassed = self.browser.find_element_by_css_selector("[value='572a1d90d336270664639177']")
             passed_notpassed.click()

             going_to_options = self.browser.find_element_by_xpath("//a[text()='Options']")
             going_to_options.click()


             #time.sleep(3)
             saving = self.browser.find_element_by_xpath("//span[text()='Save']")
             saving.click()
             #time.sleep(3)
             self.browser.execute_script("window.scrollBy(0, -500);")
             #time.sleep(5)
             alert = self.browser.find_element_by_xpath("//button[@class='close']")
             alert.click()
             assesment_title_main = self.browser.find_element_by_xpath("//a[@data-internal='']")
             assesment_title_main.click()
             publish = self.browser.find_element_by_xpath("//span[text()='Publish']")
             publish.click()
             check_box = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='publish-assess-auto-scored']")))
             check_box.click()
             radio_button = self.browser.find_element_by_xpath("//label[@data-qa='label-publish-markingWf-simple']")
             radio_button.click()
             self.browser.find_elements_by_tag_name("select")[1].click()
             self.browser.find_element_by_xpath("//option[text()='Live']").click()
             radio_button = self.browser.find_element_by_xpath("//label[@data-qa='label-publish-markingWf-simple']")
             radio_button.click()
             save_publish = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//button[data-qa='assessment-publish']")))
             save_publish.click()
        finally:
            print(1)
            #self.assessment_test()
            #self.browser.quit()

    def assessment_test_random(self):
        try:
             self.registration()
             # creating an assesment
             assesment = self.browser.find_element_by_xpath("//div[@data-href='#assessments/overview']")
             assesment.click()
             add_assesment = self.browser.find_element_by_xpath("//a[@data-qa='assessments-add']")
             add_assesment.click()
             #option_radio = WebDriverWait(self.browser, 5).until(
                #EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='label-formative']")))
             #option_radio.click()

             option_radio1 = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='label-mixed']")))
             option_radio1.click()
             option_radio1 = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH, "//label[@data-qa='label-mixed']")))
             option_radio1.click()
             #option_checkbox = self.browser.find_element_by_xpath("//label[@data-qa='print']")
             #option_checkbox.click()
             assesment_title = self.browser.find_element_by_xpath("//input[@data-qa='assessment-title']")
             assesment_title.send_keys('Random Assessment')
             assesment_code = self.browser.find_element_by_xpath("//input[@data-qa='assessment-code']")
             assesment_code.send_keys('Random Assessment')
             assesment_confim = self.browser.find_element_by_xpath("//button[@data-qa='new-assessment-save']")
             assesment_confim.click()
             # settings of the assesment
             assesment_code = self.browser.find_element_by_xpath("//input[@id='ExternalId']")
             Id = (''.join(choice(ascii_letters + digits) for i in range(7)))
             assesment_code.send_keys(Id)
             save_externalId = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='assessment-i-save']")))
             save_externalId.click()

             alert=WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//button[@class='close']")))
             alert.click()
             #alert = WebDriverWait(browser, 5).until_not(
               #EC.invisibility_of_element_located((By.XPATH, "//div[class()='alert alert-success alert-dismissible']")))
             time.sleep(2)
             go_to_options = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//div[text()='options']")))

             go_to_options.click()
             self.browser.find_elements_by_tag_name("select")[2].click()
             self.browser.find_element_by_xpath("//option[text()='After each attempt']").click()
             #time.sleep(5)
             check_box = self.browser.find_element_by_xpath("//label[@data-qa='assessment-options-show-only-status']")
             check_box.click()
             self.browser.execute_script("window.scrollBy(0, 800);")
             save_options = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//span[text()='Save']")))
             save_options.click()
             #time.sleep(3)
             self.browser.execute_script("window.scrollBy(0, -1200);")
             alert = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//button[@class='close']")))
             alert.click()
             go_to_selection = self.browser.find_element_by_xpath("//div[text()='question selection']")
             go_to_selection.click()

             #-------------------------------------------------------------------------------------------------------
             time.sleep(2)
             side_bar = WebDriverWait(self.browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//i[@class='fa fa-bars']")))
             side_bar.click()

             list_of_all_items = []
             all_items = self.browser.find_elements_by_xpath("//span[@class='lbl']")
             for element in all_items:
                 list_of_all_items.append(element.text)

             list_of_png_pictures = []
             for element in list_of_all_items:
                 if 'Collection Regression' in element:
                     list_of_png_pictures.append(element)
                 else:
                     print("Not satisfy collection")

             print(list_of_png_pictures)
             choose_collection_by_text=self.browser.find_element_by_xpath(f"//span[text()='"
                                                                          f"{list_of_png_pictures[0]}']")
             choose_collection_by_text.click()
             #-------------------------------------------------------------------------------------------------------
             select_question =  WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='table-check-all']")))
             select_question.click()
             #time.sleep(5)
             adding_question = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='manual-selection-add-questions']")))
             adding_question.click()
             #time.sleep(5)
             forms = self.browser.find_element_by_xpath("//div[text()='forms']")
             forms.click()

             adding_form = WebDriverWait(self.browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//button[@class='rs_preserve toolbarButtonSkinAdjustment button-0-1 button-1Mv2-']")))
             adding_form.click()
             adding_random_form = self.browser.find_element_by_xpath("//label[@data-qa='label-gen-form-random']")
             adding_random_form.click()

             select_questions = self.browser.find_element_by_xpath("//input[@data-qa='add-hierarchy-title']")
             select_questions.send_keys(u'\ue015'+u'\ue015')
             time.sleep(3)
             creating_form = self.browser.find_element_by_xpath("//button[@data-qa='assessment-gf-save']")
             creating_form.click()
             forms_settings = self.browser.find_element_by_xpath("//div[text()='Form A']")
             forms_settings.click()
             #time.sleep(1)
             self.browser.find_elements_by_xpath("//button[@data-qa='']")[0].click()
             first_choice = self.browser.find_element_by_xpath("//div[@data-qa='1']")
             first_choice.click()
             self.browser.find_elements_by_xpath("//div[@class='div-12z2j td-2Bgor cell-in-sorted-row-Rxf0B "
                                             "column-3JUVA']")[0].click()
             self.browser.find_elements_by_xpath("//button[@data-qa='']")[1].click()
             second_choice = self.browser.find_element_by_xpath("//div[@data-qa='2']")
             second_choice.click()
             self.browser.find_elements_by_xpath("//div[@class='div-12z2j td-2Bgor cell-in-sorted-row-Rxf0B "
                                             "column-3JUVA']")[1].click()
             self.browser.execute_script("window.scrollBy(0, -500);")
             going_to_options = self.browser.find_element_by_xpath("//a[text()='Options']")
             going_to_options.click()
             #time.sleep(2)
             assesment_scale = self.browser.find_element_by_xpath("//div[@class='easCombobox-2aPdw "
                                                               "assessmentScales-24XfV rs_preserve']")
             assesment_scale.click()
             passed_notpassed = self.browser.find_element_by_css_selector("[value='572a1d90d336270664639177']")
             passed_notpassed.click()

             going_to_options = self.browser.find_element_by_xpath("//a[text()='Options']")
             going_to_options.click()


             #time.sleep(3)
             saving = self.browser.find_element_by_xpath("//span[text()='Save']")
             saving.click()
             #time.sleep(3)
             self.browser.execute_script("window.scrollBy(0, -500);")
             #time.sleep(5)
             alert = self.browser.find_element_by_xpath("//button[@class='close']")
             alert.click()
             assesment_title_main = self.browser.find_element_by_xpath("//a[@data-internal='']")
             assesment_title_main.click()
             publish = self.browser.find_element_by_xpath("//span[text()='Publish']")
             publish.click()
             check_box = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='publish-assess-auto-scored']")))
             check_box.click()
             radio_button = self.browser.find_element_by_xpath("//label[@data-qa='label-publish-markingWf-simple']")
             radio_button.click()
             self.browser.find_elements_by_tag_name("select")[1].click()
             self.browser.find_element_by_xpath("//option[text()='Live']").click()
             radio_button = self.browser.find_element_by_xpath("//label[@data-qa='label-publish-markingWf-simple']")
             radio_button.click()
             save_publish = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//button[data-qa='assessment-publish']")))
             save_publish.click()
        finally:
            print(1)
            #self.assessment_test()
            #self.browser.quit()
