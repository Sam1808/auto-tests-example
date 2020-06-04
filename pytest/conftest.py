#Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py,
# который должен лежать в директории верхнего уровня в вашем проекте с тестами.
# Можно создавать дополнительные файлы conftest.py в других директориях,
# но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.


import pytest
from selenium import webdriver

# Опция выбора браузера
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

# запуск браузера в соответвии с опцией
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()