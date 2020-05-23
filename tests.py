import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os.path
from random import choice
from string import ascii_letters
from string import digits
from test_collection import *

def test_collection():
    Object_collection = Collection_test()
    Object_collection.collection_test()
def test_assesment():
    Object_assessment = Collection_test()
    Object_assessment.assessment_test()
