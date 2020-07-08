import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os.path
from random import choice
from string import ascii_letters
from string import digits
from test_collection import *


def test_2(domen, browser):
    object = Collection_test()
    object.registration(domen, browser)

    # creating collections
    object.creating_collection(browser)

    # ----------------------------------------------------------------------
    # question multiple choice
    object.question_multiple_choice(browser)

    # ----------------------------------------------------------------------
    # question emc
    object.question_emc(browser)

    # ----------------------------------------------------------------------
    # question mr
    #object.question_mr(browser)

    # ----------------------------------------------------------------------
    # question_either/or
    #object.question_either_or(browser)

    # ----------------------------------------------------------------------
    # question_numeric
    #object.question_numeric_specific(browser)

    # ----------------------------------------------------------------------
    # question_numeric_range
    #object.question_numeric_range(browser)

    # ----------------------------------------------------------------------
    # question_SFL
    #object.question_SFL(browser)

    # ----------------------------------------------------------------------
    # question_fill_blank_qustion
    #object.question_fill_blank_qustion(browser)

    # ----------------------------------------------------------------------
    # question_order
    #object.question_order(browser)

    # ----------------------------------------------------------------------
    # question_Match
    #object.question_Match(browser)

    # ----------------------------------------------------------------------
    # question_Hotspot
    #object.question_Hotspot(browser)

    # ----------------------------------------------------------------------
    # extended_match_question
    #object.extended_match_question(browser)

    # ----------------------------------------------------------------------
    # financial_statement_question
    #object.financial_statement_question(browser)

    # ----------------------------------------------------------------------
    # comprehensive_integrated_puzzle_question
    #object.comprehensive_integrated_puzzle_question(browser)

    # ----------------------------------------------------------------------
    # programming_question
    #object.programming_question(browser)

    # ----------------------------------------------------------------------
    # mathematical_question
    #object.mathematical_question(browser)

    # ----------------------------------------------------------------------
    # short_answer_question
    #object.short_answer_question(browser)

    # ----------------------------------------------------------------------
    # essay_question
    #object.essay_question(browser)

    # ----------------------------------------------------------------------
    # file_response_question
    #object.essay_question_2(browser)

    # ----------------------------------------------------------------------
    # file_response_question
    #object.file_response_question(browser)

    # ----------------------------------------------------------------------
    # file_response_question
    # file_response_question_2

    #object.change_status_to_live(browser)

