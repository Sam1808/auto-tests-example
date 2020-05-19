from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

links = ["http://suninjuly.github.io/file_input.html"]

for link in links:

    try:

        browser = webdriver.Chrome()
        browser.get(link)


        firstname = browser.find_element_by_name("firstname")
        firstname.send_keys('Ivan')

        lastname = browser.find_element_by_name("lastname")
        lastname.send_keys("Petrov")

        email = browser.find_element_by_name("email")
        email.send_keys("my@mail.com")

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, '1.txt')

        file_button = browser.find_element_by_css_selector("#file")
        file_button.send_keys(file_path)

        button = browser.find_element_by_css_selector(".btn-primary")
        #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()