import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

@pytest.mark.positive
def test_vwo_login_invalid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    driver.implicitly_wait(5)

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.ID, 'js-notification-box-msg')))
    error_message_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_message_element.text)
    assert error_message_element.text == "Your email, password, IP address or location did not match"

    driver.quit()
