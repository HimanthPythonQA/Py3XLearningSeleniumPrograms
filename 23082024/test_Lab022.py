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

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username,password = row
        credentials.append({"username" : username, "password" : password})
        return credentials

file_path_fromos = os.getcwd() + "/Py3xtestdata_ddt.xlsx"
print(file_path_fromos)

@pytest.mark.parametrize("user_cred",read_credentials_from_excel(file_path_fromos))
@allure.title("Verify the Invalid Login with the Excel Testdata")
@allure.description("TC#1- Invalid login check for  app.vwo.com website")
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    vwo_login(username=username, password=password)


def vwo_login(user_cred):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    driver.implicitly_wait(5)

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys('username')
    pass_input.send_keys('password')

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    result = driver.current_url
    if result !="https://app.vwo.com/#dashboard":
       ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
       WebDriverWait(driver=driver, poll_frequency=1, timeout=60, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.ID, 'js-notification-box-msg')))
       error_message_element = driver.find_element(By.ID, "js-notification-box-msg")
       print(error_message_element.text)
       assert error_message_element.text == "Your email, password, IP address or location did not match"

    else:
        # Positive test case: Login is successful
        allure.attach(driver.get_screenshot_as_png(), name="login_success", attachment_type=AttachmentType.PNG)

        # Example of verification for successful login
        dashboard_heading = driver.find_element(By.CSS_SELECTOR, "h1.dashboard-heading")
        assert dashboard_heading.text == "Dashboard", "Dashboard heading not found"

        # Capture another screenshot after successful login
        allure.attach(driver.get_screenshot_as_png(), name="dashboard", attachment_type=AttachmentType.PNG)

        print("Login successful and dashboard page verified!")
        # WebDriverWait(driver=driver , timeout=10).until(
        #     EC.visibility_of_element_located((By.ID, 'js-notification-box-msg')))

    allure.attach(driver.get_screenshot_as_png(),name="login_click", attachment_type=AttachmentType.PNG)
    driver.quit()
