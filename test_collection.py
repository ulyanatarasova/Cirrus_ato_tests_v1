import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os.path
from random import choice
from string import ascii_letters
from string import digits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Collection_test():
    password = ['1','2','3','4','5']
    username ='un1'
    link = "https://test-education.cirrus0.eu/"
    def collection_test(self):
        try:
          browser = webdriver.Chrome()
          browser.get(self.link)
          browser.implicitly_wait(10)
          # login in sistem
          login_link = browser.find_element_by_xpath("//a[@href='#']")
          login_link.click()
          login_item_username = browser.find_element_by_xpath("//input[@id='login']")
          login_item_username.send_keys(self.username)
          login_item_password = browser.find_element_by_xpath("//input[@id='view_password']")
          login_item_password.send_keys(self.password[0])
          login_item_password.send_keys(self.password[1])
          login_item_password.send_keys(self.password[2])
          login_item_password.send_keys(self.password[3])
          login_item_password.send_keys(self.password[4])
          login_button = browser.find_element_by_xpath("//button[@class='btn btn-green-filled submitButton']")
          login_button.click()
          login_author = browser.find_element_by_xpath("//a[@href='author/app']")
          login_author.click()
          # creating collections
          collection = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='infobox_block cmn-block-margin']")))
          collection.click()
          add_collection = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='add-collection']")))
          add_collection.click()
          title_of_collection = browser.find_element_by_xpath("//input[@class='input-36b7z c0113']")
          title_of_collection.send_keys('Collection')
          confim_button_collection = browser.find_element_by_xpath(
                    "//button[@class='reset-2Sxmr button-2DTz8 rs_preserve filled-success-19y_v filledSuccess-0-4']")
          confim_button_collection.click()
          # adding question in to collection
          add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-menu']")))
          add_question.click()
          choose_type_of_question = browser.find_element_by_xpath("//a[text()='Multiple choice']")
          choose_type_of_question.click()
          # settings of the question
          title1_question = browser.find_element_by_xpath("//input[@class='form-control qe-questionTitle']")
          title1_question.send_keys('question1')
          questions = browser.find_elements_by_xpath("//div[@role='textbox']")
          for question in questions:
              question.send_keys('111')
          option1 = browser.find_element_by_xpath("//label[@class='']")
          option1.click()

          button_save_close = browser.find_element_by_xpath("//button[@data-qa='question-editor-actions-save-close']")
          button_save_close.click()
        finally:
          browser.quit()

    def assessment_test(self):
         try:
             browser = webdriver.Chrome()
             browser.get(self.link)
             browser.implicitly_wait(10)
             # login in sistem
             login_link = browser.find_element_by_xpath("//a[@href='#']")
             login_link.click()
             login_item_username = browser.find_element_by_xpath("//input[@id='login']")
             login_item_username.send_keys(self.username)
             login_item_password = browser.find_element_by_xpath("//input[@id='view_password']")
             login_item_password.send_keys(self.password[0])
             login_item_password.send_keys(self.password[1])
             login_item_password.send_keys(self.password[2])
             login_item_password.send_keys(self.password[3])
             login_item_password.send_keys(self.password[4])
             login_button = browser.find_element_by_xpath("//button[@class='btn btn-green-filled submitButton']")
             login_button.click()
             login_author = browser.find_element_by_xpath("//a[@href='author/app']")
             login_author.click()
             # creating an assesment
             assesment = browser.find_element_by_xpath("//div[@data-href='#assessments/overview']")
             assesment.click()
             add_assesment = browser.find_element_by_xpath("//a[@data-qa='assessments-add']")
             add_assesment.click()
             option_radio = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='label-formative']")))
             option_radio.click()

             option_radio1 = WebDriverWait(browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='label-mixed']")))
             option_radio1.click()
             option_checkbox = browser.find_element_by_xpath("//label[@data-qa='print']")
             option_checkbox.click()
             assesment_title = browser.find_element_by_xpath("//input[@data-qa='assessment-title']")
             assesment_title.send_keys('Assesment title')
             assesment_code = browser.find_element_by_xpath("//input[@data-qa='assessment-code']")
             assesment_code.send_keys('1234567')
             assesment_confim = browser.find_element_by_xpath("//button[@data-qa='new-assessment-save']")
             assesment_confim.click()
             # settings of the assesment
             assesment_code = browser.find_element_by_xpath("//input[@id='ExternalId']")
             Id = (''.join(choice(ascii_letters + digits) for i in range(7)))
             assesment_code.send_keys(Id)
             save_externalId = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='assessment-i-save']")))
             save_externalId.click()

             alert=browser.find_element_by_xpath("//button[@class='close']")
             alert.click()
             #alert = WebDriverWait(browser, 5).until_not(
               #EC.invisibility_of_element_located((By.XPATH, "//div[class()='alert alert-success alert-dismissible']")))
             go_to_options = WebDriverWait(browser, 5).until(
                  EC.element_to_be_clickable((By.XPATH,"//div[text()='options']")))

             go_to_options.click()
             browser.find_elements_by_tag_name("select")[2].click()
             browser.find_element_by_xpath("//option[text()='After each attempt']").click()
             #time.sleep(5)
             check_box = browser.find_element_by_xpath("//label[@data-qa='assessment-options-show-only-status']")
             check_box.click()
             browser.execute_script("window.scrollBy(0, 800);")
             save_options = browser.find_element_by_xpath("//span[text()='Save']")
             save_options.click()
             #time.sleep(3)
             browser.execute_script("window.scrollBy(0, -1200);")
             alert = browser.find_element_by_xpath("//button[@class='close']")
             alert.click()
             go_to_selection = browser.find_element_by_xpath("//div[text()='question selection']")
             go_to_selection.click()
             #time.sleep(5)
             select_question =  WebDriverWait(browser, 5).until(
                 EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='table-check-all']")))
             select_question.click()
             #time.sleep(5)
             adding_question = browser.find_element_by_xpath("//button[@data-qa='manual-selection-add-questions']")
             adding_question.click()
             #time.sleep(5)
             forms = browser.find_element_by_xpath("//div[text()='forms']")
             forms.click()
             adding_form = browser.find_element_by_xpath("//button[@data-qa='assessment-ga-create']")
             adding_form.click()
             adding_fixed_form = browser.find_element_by_xpath("//label[@data-qa='label-gen-form-fixed']")
             adding_fixed_form.click()
             creating_form = browser.find_element_by_xpath("//button[@data-qa='assessment-gf-save']")
             creating_form.click()
             forms_settings = browser.find_element_by_xpath("//div[text()='Form A']")
             forms_settings.click()
             #time.sleep(1)
             browser.find_elements_by_xpath("//button[@data-qa='']")[0].click()
             first_choice = browser.find_element_by_xpath("//div[@data-qa='1']")
             first_choice.click()
             browser.find_elements_by_xpath("//div[@class='div-12z2j td-2Bgor cell-in-sorted-row-Rxf0B column-3JUVA']")[0].click()
             browser.find_elements_by_xpath("//button[@data-qa='']")[1].click()
             second_choice = browser.find_element_by_xpath("//div[@data-qa='2']")
             second_choice.click()
             browser.find_elements_by_xpath("//div[@class='div-12z2j td-2Bgor cell-in-sorted-row-Rxf0B column-3JUVA']")[1].click()
             browser.execute_script("window.scrollBy(0, -500);")
             going_to_options = browser.find_element_by_xpath("//a[text()='Options']")
             going_to_options.click()
             #time.sleep(2)
             assesment_scale = browser.find_element_by_xpath("//div[@class='easCombobox-2aPdw assessmentScales-24XfV rs_preserve']")
             assesment_scale.click()
             passed_notpassed = browser.find_element_by_css_selector("[value='572a1d90d336270664639177']")
             passed_notpassed.click()

             browser.execute_script("window.scrollBy(0, 500);")

             #time.sleep(3)
             saving = browser.find_element_by_xpath("//button[@data-qa='save-options-form']")
             saving.click()
             #time.sleep(3)
             browser.execute_script("window.scrollBy(0, -500);")
             #time.sleep(5)
             alert = browser.find_element_by_xpath("//button[@class='close']")
             alert.click()
             assesment_title_main = browser.find_element_by_xpath("//a[@data-internal='']")
             assesment_title_main.click()
             publish = browser.find_element_by_xpath("//span[text()='Publish']")
             publish.click()
             check_box = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='publish-assess-auto-scored']")))
            check_box.click()
            radio_button = browser.find_element_by_xpath("//label[@data-qa='label-publish-markingWf-simple']")
            radio_button.click()
            browser.find_elements_by_tag_name("select")[1].click()
            browser.find_element_by_xpath("//option[text()='Live']").click()
            save_publish = browser.find_element_by_xpath("//button[@data-qa='assessment-publish']")
            save_publish.click()
        finally:
            browser.quit()
