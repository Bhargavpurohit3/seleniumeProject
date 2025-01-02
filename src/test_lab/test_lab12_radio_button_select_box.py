import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_practice_html():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")
    firstname.send_keys("bhargav")

    lastname = driver.find_element(By.XPATH, "//input[@name='lastname']")
    lastname.send_keys("purohit")

    