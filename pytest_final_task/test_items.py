link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_button_exist(browser):
    browser.get(link)
    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except:
        assert False, "Cannot find cart button"
