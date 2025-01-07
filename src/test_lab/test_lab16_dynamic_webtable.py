from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import allure
import time

@allure.title("dybnamic table which changeb the raw and colum as per data")
def test_dynamic():

    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")

    table_head = driver.find_element(By.XPATH, "//table[contains(@summary,'Sample Table')]/thead")
    head_raw = table_head.find_elements(By.TAG_NAME, "tr")

    table_foot = driver.find_element(By.XPATH, "//table[contains(@summary,'Sample Table')]/tfoot")
    foot_raw = table_foot.find_elements(By.TAG_NAME, "tr")

    table_body = driver.find_element(By.XPATH, "//table[contains(@summary,'Sample Table')]/tbody")
    body_raw = table_body.find_elements(By.TAG_NAME, "tr")

    """print(len(head_raw))
    print(len(foot_raw))
    print(len(body_raw))"""

    for data in body_raw:
        col_data = data.find_elements(By.TAG_NAME, "td")
        for cell in col_data:
            print(cell.text)