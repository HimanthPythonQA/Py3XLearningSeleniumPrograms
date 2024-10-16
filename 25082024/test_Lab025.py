import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *
import os


@pytest.mark.positive
def test_vwo_login_select():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        # staleElementRefrenceException
        textarea = driver.find_element(By.NAME,"q")
        driver.refresh()
        # Document HTML might change--refresh
        # element--textarea--not available now after refreshing
        # refresh,navigate to other page, change in DOM elements
        textarea.send_keys("the testing academy")
    except StaleElementReferenceException as see:
        print(see)
        print("stale element reference")
        textarea = driver.find_element(By.NAME, "q")
        textarea.send_keys("the testing academy")


    time.sleep(4)