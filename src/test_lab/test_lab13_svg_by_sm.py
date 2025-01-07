import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_svg():

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()


    cookie = driver.find_element(By.XPATH, "//input[@value='I agree']")
    cookie.click()

    # Locate Gujarat using XPath for SVG and aria-label
    list_of_tate = driver.find_elements(By.XPATH,
                        "//*[name()= 'svg']/*[name()= 'g'][7]/*[name()= 'g']/*[name()= 'g']/*[name()= 'path']")
    for state in list_of_tate:
        area = state.get_attribute("aria-label")
        if "Gujarat" in area:
            state.click()
            time.sleep(10)
            break
        
