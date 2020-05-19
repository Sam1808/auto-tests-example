from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

links = ["http://suninjuly.github.io/selects2.html"]

for link in links:

    try:

        browser = webdriver.Chrome()
        browser.get(link)


        num1 = browser.find_element_by_css_selector("#num1")
        num2 = browser.find_element_by_css_selector("#num2")

        print(num1.text, num2.text, flush=True)

        total = int(num1.text) + int(num2.text)
        print(type(total), total, flush=True)

        select = Select(browser.find_element_by_css_selector("#dropdown"))
        select.select_by_value(str(total))

        button = browser.find_element_by_css_selector(".btn-default")
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()