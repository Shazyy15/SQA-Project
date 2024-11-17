
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://localhost:8080/login')

driver.find_element(By.ID, 'username').send_keys('test_user')
driver.find_element(By.ID, 'password').send_keys('password123')
driver.find_element(By.ID, 'login_button').click()

assert "Dashboard" in driver.title
driver.quit()
