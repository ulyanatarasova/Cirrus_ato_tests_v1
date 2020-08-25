import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os.path
from random import choice
from string import ascii_letters
from string import digits
from .body_of_collection_tests import Collection_test




@pytest.mark.main
def test_creating_collection(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.creating_collection(varibles, browser)


@pytest.mark.main
def test_question_multiple_choice(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_multiple_choice_test(varibles, browser)


@pytest.mark.main
def test_question_emc(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_emc(varibles, browser)


@pytest.mark.main
def test_question_mr(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_mr(varibles, browser)


@pytest.mark.main
def test_question_either_or(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_either_or(varibles, browser)


@pytest.mark.main
def test_question_numeric_specific(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_numeric_specific(varibles, browser)


@pytest.mark.main
def test_question_numeric_range(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_numeric_range(varibles, browser)


@pytest.mark.main
def test_question_SFL(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_SFL(varibles, browser)


@pytest.mark.main
def test_question_fill_blank(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_fill_blank(varibles, browser)


@pytest.mark.main
def test_question_order(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_order(varibles, browser)


@pytest.mark.main
def test_question_Match(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_Match(varibles, browser)


@pytest.mark.main
def test_question_Hotspot(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.question_Hotspot(varibles, browser)


@pytest.mark.main
def test_extended_match_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.extended_match_question(varibles, browser)

@pytest.mark.main
def test_drag_and_drop_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.drag_and_drop_question(varibles, browser)

@pytest.mark.main
def test_comprehensive_integrated_puzzle_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.comprehensive_integrated_puzzle_question(varibles, browser)

@pytest.mark.main
def test_financial_statement_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.financial_statement_question(varibles, browser)

@pytest.mark.main
def test_programming_question(domen, browser, varibles): #numeric
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.programming_question(varibles, browser)

@pytest.mark.main
def test_mathematical_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.mathematical_question(varibles, browser)

@pytest.mark.main
def test_short_answer_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.short_answer_question(varibles, browser)

@pytest.mark.main
def test_essay_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.essay_question(varibles, browser)

@pytest.mark.main
def test_file_response_question(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.file_response_question(varibles, browser)

@pytest.mark.main
def test_sectione(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.section(varibles, browser)

@pytest.mark.main
def test_page_welcome(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.page_welcome(varibles, browser)

@pytest.mark.main
def test_page_finish(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.page_finish(varibles, browser)

@pytest.mark.main
def test_page_other(domen, browser, varibles):
    object = Collection_test(varibles['user']['login'], varibles['user']['password'])
    object.login(domen, browser)
    object.page_other(varibles, browser)

