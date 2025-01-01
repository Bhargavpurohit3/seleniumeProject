import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("dropdon")
@allure.description("dropdown manu")

def test_drop_down():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dp_down = driver.find_element(By.XPATH,"//select[@id='dropdown']")
    dp_down_value = Select(dp_down)

    dp_down_value.select_by_visible_text("Option 2")
    time.sleep(1)
    dp_down_value.select_by_index(1)
    time.sleep(1)
    dp_down_value.select_by_visible_text("Option 2")
    time.sleep(1)
    dp_down_value.select_by_index(1)
    time.sleep(5)

    driver.quit()