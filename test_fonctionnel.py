from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def open_chrome():
    driver  = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://dev-passion76.fr/assureplus/")

    buttonlogin = driver.find_element(By.CLASS_NAME,"contact-submit")

    buttonlogin.click()

    inputemail = driver.find_element(By.CSS_SELECTOR,'input[formControlName="emailOrUsername"]')
    inputpassword = driver.find_element(By.CSS_SELECTOR,'input[formControlName="password"]')

    inputemail.send_keys("test-user@gmail.fr")
    inputpassword.send_keys("testpassword")
    inputpassword.send_keys(Keys.ENTER)
