import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os.path
from random import choice
from string import ascii_letters
from string import digits
from tests_for_assessment import *

#def test_assesment_fixed():
    #Object_assessment = Collection_test()
    #Object_assessment.assessment_test()

def test_assesment_random():
    Object_assessment = Collection_test()
    Object_assessment.assessment_test_random()