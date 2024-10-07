import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select

@pytest.mark.positive
def test_flipkart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    search_input = driver.find_element(By.NAME,"q")
    search_input = driver.find_element(By.XPATH, "//input[@name='q']")
    search_input.send_keys("AC")

    svg_list = driver.find_element(By.XPATH,"//*[local-name()='svg']")
    svg_list.click()

    time.sleep(5)
    driver.close()