from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()
    #alert = browser.switch_to.alert
    #alert.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value")
    y = calc(int(x.text))

    print(x, y, flush=True)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)


    button = browser.find_element_by_css_selector(".btn-primary")

    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
