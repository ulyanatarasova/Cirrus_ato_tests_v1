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
    password = ['u','l','y','a','n','a']
    username ='ulyana'
    
    def registration(self, domen , browser):
        browser.get(domen)
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
        login_item_password.send_keys(self.password[5])
        login_button = browser.find_element_by_xpath("//button[@class='btn btn-green-filled submitButton']")
        login_button.click()
        login_author = browser.find_element_by_xpath("//a[@href='author/app']")
        login_author.click()

    def creating_collection(self, browser):
        open_tab_collection = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,
                                                                                      "//div[@class='infobox_block cmn-block-margin']")))
        open_tab_collection.click()

        time.sleep(3)
        add_collection = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                          "//a[@id='add-collection']")))
        add_collection.click()

        title_of_collection = browser.find_element_by_xpath("//input[@class='input-36b7z c0113']")
        title_of_collection.send_keys('Collection Regression')

        confim_button_collection = browser.find_element_by_xpath(
            "//button[@class='reset-2Sxmr button-2DTz8 rs_preserve filled-success-19y_v filledSuccess-0-4']")
        confim_button_collection.click()

        alert = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
        alert.click()

    def question_multiple_choice(self ,browser):
        time.sleep(5)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = browser.find_element_by_xpath("//a[text()='Multiple choice']")
        choose_type_of_question.click()
        # settings of the question
        #title_question = self.browser.find_element_by_xpath("//input[@class='form-control qe-questionTitle']")
        #title_question.send_keys('Multiple choice')
        #questions = self.browser.find_elements_by_xpath("//div[@role='textbox']")

        #for question in questions:
            #question.send_keys('111')

        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Multiple choice')
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')
        browser.find_elements_by_xpath("//div[@role='textbox']")[2].send_keys('2')
        browser.find_elements_by_xpath("//div[@role='textbox']")[3].send_keys('3')

        option = browser.find_element_by_xpath("//label[@class='']")
        option.click()

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def question_emc(self, browser):
        try:
           add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
           add_question.click()
        except:
            print("fail")

        choose_type_of_question =  WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                    "//a[text()='Extended multiple choice']")))
        choose_type_of_question.click()
        # settings of the question
        questions = browser.find_elements_by_xpath("//div[@role='textbox']")
        s = 0
        for question in questions:
            s = s + 1
            question.send_keys(f'Extended multiple choice {s}')

        browser.execute_script("window.scrollBy(0, -400);")
        browser.find_elements_by_xpath("//label[@class='']")[0].click()
        browser.execute_script("window.scrollBy(0, 500);")
        browser.find_elements_by_xpath("//label[@class='']")[2].click()
        # self.browser.execute_script("window.scrollBy(0, -400);")
        # option = self.browser.find_element_by_xpath("//label[@wfd-id='4755']")
        # self.browser.execute_script("window.scrollBy(0, 500);")
        # option = self.browser.find_element_by_xpath("//label[@wfd-id='4484']")
        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()


    def question_mr(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Multiple response']")))
        choose_type_of_question.click()
        # settings of the question
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Multiple response')
        #setting of the question
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')

        browser.find_elements_by_xpath("//div[@role='textbox']")[2].send_keys('2')
        browser.find_elements_by_xpath("//div[@role='textbox']")[3].send_keys('3')

        browser.find_elements_by_xpath("//label[@class='']")[0].click()

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def question_either_or(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                      "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Either/Or']")))
        choose_type_of_question.click()
        # settings of the question
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Either/Or')
        #setting of the question
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')

        browser.find_elements_by_xpath("//div[@role='textbox']")[2].send_keys('2')

        browser.find_elements_by_xpath("//label[@class='']")[0].click()

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def question_numeric_specific(self, browser): #specific value
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Numeric']")))
        choose_type_of_question.click()

        browser.find_element_by_xpath("//div[@role='textbox']").send_keys('Numeric Specific Value')
        #value
        send_value = browser.find_element_by_xpath("//input[@class='input-36b7z']")
        send_value.send_keys('1')

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def question_numeric_range(self, browser):  # range
            time.sleep(2)
            add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                      "@id='add-menu']")))
            add_question.click()
            choose_type_of_question = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Numeric']")))
            choose_type_of_question.click()

            browser.find_element_by_xpath("//div[@role='textbox']").send_keys('Numeric Range')
            # value
            browser.find_element_by_xpath("//label[@class='']").click()
            time.sleep(2)

            browser.find_elements_by_xpath("//input[@class='input-36b7z']")[1].send_keys(1)
            browser.find_elements_by_xpath("//input[@class='input-36b7z']")[2].send_keys(2)


            button_save_close = browser.find_element_by_xpath(
                "//button[@data-qa='question-editor-actions-save-close']")
            button_save_close.click()

    def question_SFL(self, browser):
            time.sleep(2)
            add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                      "@id='add-menu']")))
            add_question.click()
            choose_type_of_question = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Select from list']")))
            choose_type_of_question.click()

            browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('1234 no')

            #self.browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys( (u'\ue009'+"a") )

            browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys( u'\ue008'+ u'\ue012'+ u'\ue012')

            browser.find_element_by_xpath("//a[@id='add-blank']").click()
            browser.find_element_by_xpath("//input[@data-qa='blanked-words']").send_keys('No')

            button_save_close = browser.find_element_by_xpath(
                "//button[@data-qa='question-editor-actions-save-close']")
            button_save_close.click()

    def question_fill_blank_qustion(self, browser):
            time.sleep(2)
            add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                      "@id='add-menu']")))
            add_question.click()
            choose_type_of_question = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Fill in the blank']")))
            choose_type_of_question.click()

            browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('1234 no')

            #self.browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys( (u'\ue009'+"a") )

            browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys( u'\ue008'+ u'\ue012'+ u'\ue012')

            browser.find_element_by_xpath("//a[@id='add-blank']").click()
            browser.find_element_by_xpath("//input[@data-qa='blanked-words']").send_keys('No')

            button_save_close = browser.find_element_by_xpath("//button[@data-qa='question-editor-actions-save-close']")
            button_save_close.click()

    def question_order(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Order']")))
        choose_type_of_question.click()

        #self.browser.find_element_by_xpath("//a[@data-qa='add-alternative-button']").click()
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Order')
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')
        browser.find_elements_by_xpath("//div[@role='textbox']")[2].send_keys('2')
        browser.find_elements_by_xpath("//div[@role='textbox']")[3].send_keys('3')
        #self.browser.find_elements_by_xpath("//div[@role='textbox']")[4].send_keys('1234567')
        browser.find_element_by_xpath("//a[@data-qa='add-alternative-button']").click()
        browser.find_elements_by_xpath("//div[@role='textbox']")[0]
        browser.find_elements_by_xpath("//div[@role='textbox']")[1]
        browser.find_elements_by_xpath("//div[@role='textbox']")[2]
        browser.find_elements_by_xpath("//div[@role='textbox']")[3]

        time.sleep(3)
        browser.find_elements_by_xpath("//div[@role='textbox']")[4].send_keys('4')

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def question_Match(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Match']")))
        choose_type_of_question.click()

        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Match')
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')
        browser.find_elements_by_xpath("//div[@role='textbox']")[2].send_keys('2')
        browser.find_elements_by_xpath("//div[@role='textbox']")[3].send_keys('3')
        browser.find_elements_by_xpath("//div[@role='textbox']")[4].send_keys('4')
        browser.find_elements_by_xpath("//div[@role='textbox']")[5].send_keys('5')
        browser.find_elements_by_xpath("//div[@role='textbox']")[6].send_keys('6')

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def question_Hotspot(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Hotspot']")))
        choose_type_of_question.click()

        browser.find_element_by_xpath("//div[@role='textbox']").send_keys('Hotspot')

        browser.find_element_by_xpath("//button[@data-qa='add-file-button']").click()
        #алгоритм для нахождения всех файлов из списка и выбор из этого списка только файлов png and jpg
        list_of_all_items = []
        all_items = browser.find_elements_by_xpath("//div[@class='listViewItem__column']")
        for element in all_items:
            print(element.text)
            list_of_all_items.append(element.text)
        list_of_png_pictures =[]
        for element in list_of_all_items:
            if '.png' in element:
                list_of_png_pictures.append(element)
            else:
                print("No pictures were find")
        print(list_of_png_pictures)
        browser.find_element_by_xpath(f"//div[text()='{list_of_png_pictures[0]}']").click()
        # алгоритм для нахождения всех файлов из списка и выбор из этого списка только файлов png and jpg
            #send_keys('C:\Math2020\geometr\Корейский.png')
        #current_dir = os.path.abspath(os.path.dirname(__file__))
        #print(current_dir)
        #file_path = os.path.join(current_dir, 'Корейский.png')

        #for upload file use that code
        #send_file=self.browser.find_element_by_xpath("//input[@type='file']")
        #send_file.send_keys('C:/Users/Ulyana/Documents/Cirrus/Корейский.png')
        #print(root.position())
        # for upload file use that code

        time.sleep(2)
        browser.find_element_by_xpath("//label[@data-action='ellipse']").click()
        print(1)
        element = browser.find_element_by_tag_name("image")
        print(1)
        action = ActionChains(browser)
        hov = action.drag_and_drop_by_offset(element, 20, 20).perform()

        hov_2 = action.drag_and_drop_by_offset(element, 70, 70).perform()

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def extended_match_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Extended match']")))
        choose_type_of_question.click()

        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Extended match')
        #first fill
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')
        browser.find_elements_by_xpath("//div[@role='textbox']")[2].send_keys('2')
        #second fill
        browser.find_elements_by_xpath("//div[@role='textbox']")[3].send_keys('1')
        browser.find_elements_by_xpath("//div[@role='textbox']")[4].send_keys('2')

        #clicking button "switch mode"
        browser.find_element_by_xpath("//button[@id='qe-ext_match_mode']").click()

        #first connection
        browser.find_elements_by_tag_name("circle")[15].click()
        time.sleep(1)
        browser.find_elements_by_tag_name("circle")[17].click()

        #second connection
        browser.find_elements_by_tag_name("circle")[17].click()
        time.sleep(1)
        browser.find_elements_by_tag_name("circle")[19].click()

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def financial_statement_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Financial statement']")))
        choose_type_of_question.click()
        #question body
        body=WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH,"//div[@role='textbox']")))
        body.send_keys('Financial statement')

        section_header = browser.find_element_by_xpath("//input[@data-qa='fs-section-title']")
        section_header.send_keys("Some header")

        #fill first title
        browser.find_elements_by_xpath("//input[@data-qa='fs-title']")[0].send_keys("First title_1")
        browser.find_elements_by_xpath("//input[@data-qa='fs-title']")[1].send_keys("First title_2")
        #fill first debit
        browser.find_elements_by_xpath("//input[@data-qa='fs-debit']")[0].send_keys("1")
        browser.find_elements_by_xpath("//input[@data-qa='fs-debit']")[1].send_keys("2")
        #fill first credit
        browser.find_elements_by_xpath("//input[@data-qa='fs-credit']")[0].send_keys("3")
        browser.find_elements_by_xpath("//input[@data-qa='fs-credit']")[1].send_keys("4")

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def comprehensive_integrated_puzzle_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Comprehensive Integrated Puzzle']")))
        choose_type_of_question.click()
        # question body
        body = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']")))
        body.send_keys('Comprehensive Integrated Puzzle')

        #colum header
        browser.find_elements_by_xpath("//input[@type='text']")[4].send_keys("Colum header")
        #row header
        browser.find_elements_by_xpath("//input[@type='text']")[5].send_keys("Row header")
        #body question
        browser.find_elements_by_xpath("//input[@type='text']")[6].send_keys("Some body")

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def programming_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Programming']")))
        choose_type_of_question.click()
        # question body
        body = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']")))
        body.send_keys('Programming')

        browser.find_element_by_xpath("//a[text()='Test cases']").click()

        browser.find_element_by_xpath("//textarea[@class='ace_text-input']").send_keys("case = Test 7+5\n"
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
                                                                                            "output = 2048")

        browser.find_element_by_xpath("//a[text()='Requested files']").click()
        browser.find_element_by_xpath("//button[text()='Create']").click()
        browser.find_element_by_xpath("//input[@value='']").send_keys("index.js")
        browser.find_element_by_xpath("//button[@class='reset-2Sxmr button-2DTz8 rs_preserve filled-success-19y_v filledSuccess-0-4']").click()
        browser.find_element_by_xpath("//textarea[@class='ace_text-input']").send_keys("const readline = "
                                                                                            "require('readline');\n"
                                                                                            "const sum = (num1, num2) => {\n"
                                                                                            "    //This function should return sum of values\n"
                                                                                            "    return null;\n"
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
                                                                                            "});")
        #colum header

        browser.find_element_by_xpath("//a[text()='Execution options']").click()
        browser.find_elements_by_tag_name("select")[2].click()

        browser.find_elements_by_xpath("//option[@value='1']")[0].click()

        browser.find_elements_by_tag_name("select")[4].click()
       
        browser.find_elements_by_xpath("//option[@value='1']")[2].click()
        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def mathematical_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                              "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
             EC.element_to_be_clickable((By.XPATH, "//a[text()='Mathematical question']")))
        choose_type_of_question.click()
        # question body
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Mathematical question')
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')
        browser.find_element_by_xpath("//textarea[@class='solution-attr']").send_keys('1')
        browser.find_element_by_xpath("//span[text()='Save']").click()



        alert = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
        alert.click()
        browser.find_element_by_xpath("//span[@aria-hidden='true']").click()
        browser.find_element_by_xpath("//a[text()='Question set']").click()

        browser.find_element_by_xpath("//button[@data-qa='sowiso-set-add']").click()

        title = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='textbox']")))
        title.send_keys("Mathematical question_2")
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('2')
        browser.find_element_by_xpath("//textarea[@class='solution-attr']").send_keys('2')
        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def short_answer_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                              "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
             EC.element_to_be_clickable((By.XPATH, "//a[text()='Short answer']")))
        choose_type_of_question.click()
        # question body
        browser.find_element_by_xpath("//div[@role='textbox']").send_keys('Short answer')
        browser.find_element_by_xpath("//input[@class='qe-sa-alt_text border']").send_keys('1')

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def essay_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Essay']")))
        choose_type_of_question.click()
        # question body
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Essay withot MS')
        #self.browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def essay_question_2(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                      "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Essay']")))
        choose_type_of_question.click()
            # question body
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('Essay with MS')
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def file_response_question(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                  "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='File response']")))
        choose_type_of_question.click()
        # question body
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('File response withot MS')
        #self.browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')

        button_save_close = browser.find_element_by_xpath(
            "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def file_response_question_2(self, browser):
        time.sleep(2)
        add_question = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                                      "@id='add-menu']")))
        add_question.click()
        choose_type_of_question = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='File response']")))
        choose_type_of_question.click()
            # question body
        browser.find_elements_by_xpath("//div[@role='textbox']")[0].send_keys('File response with MS')
        browser.find_elements_by_xpath("//div[@role='textbox']")[1].send_keys('1')

        button_save_close = browser.find_element_by_xpath(
                "//button[@data-qa='question-editor-actions-save-close']")
        button_save_close.click()

    def change_status_to_live(self, browser):
        alert = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
        alert.click()
        #alert_off = WebDriverWait(browser, 10).until_not(
            #EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
    
        #self.browser.find_element_by_xpath("//span[@aria-hidden='true']").click()
        select_all=WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[@data-qa='table-check-all']")))
        select_all.click()
        action = browser.find_element_by_xpath("//button[@data-qa='collection-actions']")
        action.click()
        change_status = browser.find_element_by_xpath("//div[text()='Change status']")
        change_status.click()
        browser.find_element_by_xpath("//div[@data-qa='submenu-change-status-draft']")
        live = browser.find_element_by_xpath("//div[@data-qa='submenu-change-status-live']")
        live.click()
        confim_button = browser.find_element_by_xpath("//span[text()='Yes']")
        confim_button.click()

    




