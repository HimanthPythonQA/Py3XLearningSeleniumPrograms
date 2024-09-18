from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://google.com")



def test_sample():
    driver = webdriver.Edge()
    driver.get("https://www.google.com")
    assert driver.current_url == "https://www.google.com"