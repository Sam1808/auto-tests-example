from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    #browser.implicitly_wait(2)
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element_by_css_selector("#book")
    button.click()

    x = browser.find_element_by_css_selector("#input_value")
    y = calc(int(x.text))

    print(x, y, flush=True)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)


    new_button = browser.find_element_by_css_selector("#solve")

    new_button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
