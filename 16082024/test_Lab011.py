import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options


@pytest.mark.positive

def test_vwo_login_invalid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    driver.implicitly_wait(5)

    email_input = driver.find_element(By.CSS_SELECTOR,"[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR,"[name='password']")

    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")

    button_sunmit_element = driver.find_element(By.ID,"js-login-btn")
    button_sunmit_element.click()

    error_message_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_message_element.text)
    assert error_message_element.text == "Your email, password, IP address or location did not match"