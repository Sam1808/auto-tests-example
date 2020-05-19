from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

links = ["http://suninjuly.github.io/get_attribute.html"]

for link in links:

    try:

        browser = webdriver.Chrome()
        browser.get(link)

        box = browser.find_element_by_css_selector("#treasure")
        x = box.get_attribute("valuex")
        print(x)
        #x_element = browser.find_element_by_css_selector("#input_value")
        #x = x_element.text

        y = calc(x)

        input = browser.find_element_by_css_selector("#answer")
        input.send_keys(y)

        checkbox = browser.find_element_by_css_selector("#robotCheckbox")
        checkbox.click()

        radio = browser.find_element_by_css_selector("#robotsRule")
        radio.click()

        button = browser.find_element_by_css_selector(".btn-default")
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()