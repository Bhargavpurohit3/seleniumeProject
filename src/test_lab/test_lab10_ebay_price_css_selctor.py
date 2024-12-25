import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from openpyxl import Workbook



@allure.title("Ebay search and listing")
@allure.description("search mac  ini in ebay")
def test_ebay_macmini():

    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    search_box = driver.find_element(By.ID, value="gh-ac")
    search_box.send_keys("macmini")
    submit = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    submit.click()

    item = driver.find_elements(By.CSS_SELECTOR, ".s-item")

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Ebay screapper"

    sheet.append(["name", "price"])

    for i in item:

        name = i.find_element(By.CLASS_NAME, "s-item__title").text
        price = i.find_element(By.CLASS_NAME, "s-item__price").text

        sheet.append([name, price])

        print(f"\nname is {name} , value prove is  .{price} ")

    workbook.save("eBay mini data.xlsx")
    print("all data added succsesfully")

    driver.quit()