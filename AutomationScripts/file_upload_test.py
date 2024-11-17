
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://localhost:8080/upload')

driver.find_element(By.ID, 'file_input').send_keys('/path/to/file.xlsx')
driver.find_element(By.ID, 'upload_button').click()

assert "Upload Successful" in driver.page_source
driver.quit()
