import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest

def test_register_opencart():

    open_cart = webdriver.Chrome()
    open_cart.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name = open_cart.find_element(By.XPATH,"//input[@id='input-firstname']")
    last_name = open_cart.find_element(By.XPATH,"//input[@id='input-lastname']")
    email = open_cart.find_element(By.XPATH,"//input[@id='input-email']")
    telephone = open_cart.find_element(By.XPATH,"//input[@id='input-telephone']")
    first_name.send_keys("bhargav")
    last_name.send_keys("purohit")
    email.send_keys("bhargoav@gmail.com")
    telephone.send_keys("94089101893")

    password = open_cart.find_element(By.XPATH,"//input[@id='input-password']")
    conf_password = open_cart.find_element(By.XPATH,"//input[@id='input-confirm']")
    password.send_keys("b@1122")
    conf_password.send_keys("b@1122")

    time.sleep(5)
    check_box = open_cart.find_element(By.XPATH,"//input[@name='agree']")
    check_box.click()

    '''
    checkbox = WebDriverWait(open_cart,1).until(EC.presence_of_element_located((By.XPATH,"//input[@name='agree']")))
    open_cart.execute_script("arguments[0].click();",checkbox)
    You have to learn about this because u dont know how this is execute
    
    task confirm bit complex but learned 
    '''

    time.sleep(1)

    submit = open_cart.find_element(By.XPATH,"//input[@class='btn btn-primary']")
    submit.click()


    time.sleep(5)
    open_cart.quit()