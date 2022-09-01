from selenium import webdriver
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Remote(command_executor='http://localhost:4444', options=chrome_options)
driver.get("http://www.baidu.com")
