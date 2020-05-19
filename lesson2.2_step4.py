from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

links = ["http://suninjuly.github.io/execute_script.html"]

for link in links:

    try:

        browser = webdriver.Chrome()
        browser.get(link)


        x = browser.find_element_by_css_selector("#input_value")
        y = calc(int(x.text))

        print(x, y, flush=True)


        input = browser.find_element_by_css_selector("#answer")
        input.send_keys(y)

        checkbox = browser.find_element_by_css_selector("#robotCheckbox")
        browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)

        checkbox.click()

        radio = browser.find_element_by_css_selector("#robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
        radio.click()



        button = browser.find_element_by_css_selector(".btn-primary")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()