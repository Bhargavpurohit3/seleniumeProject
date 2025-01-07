from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import allure
import time


@allure.description("testing_webdriver")
@allure.title("webdiver")

def test_web_driver():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    raw_tab = driver.find_elements(By.XPATH, "//table[contains(@id,'customers')]/tbody/tr")
    raw = len(raw_tab)
    col_tab = driver.find_elements(By.XPATH, "//table[contains(@id,'customers')]/tbody/tr[2]/td")
    col = len(col_tab)
    for i in range(2, raw+1):
        for j in range(1, col+1):

            main_xpath = f"//table[contains(@id,'customers')]/tbody/tr[{i}]/td[{j}]"
            data = driver.find_element(By.XPATH, main_xpath).text

            print(data, end=" old \n")



#we have completed ths cases with many variation !!!


def test_web_table_dyn():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    raw_tab = driver.find_element(By.XPATH, "//table[contains(@id,'customers')]/tbody")
    raw_dat = raw_tab.find_elements(By.TAG_NAME, "tr")

    for i in raw_dat:
        data = i.find_elements(By.TAG_NAME, "td")
        print("\n")
        for j in data:
            print(j.text)



#we have completed ths cases with many variation !!!
