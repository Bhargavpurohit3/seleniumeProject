from selenium import webdriver

def test_vwo_login():
  driver = webdriver.Chrome()
  driver.get("https://app.vwo.com")
  page_src_code=driver.page_source
  print(page_src_code)
