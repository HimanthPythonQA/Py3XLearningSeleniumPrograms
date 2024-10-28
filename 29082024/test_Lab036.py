import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_webtables_orangrHRM():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    # driver.maximize_window()

    # all rows
    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    row_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    print(row)

    # all columns
    columns_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    columns = len(columns_elements)
    print(columns)

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, columns + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennet is in {country_text}")