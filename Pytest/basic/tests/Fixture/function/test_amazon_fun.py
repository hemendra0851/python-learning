from pytest import mark

@mark.browser
class AmznTest:

    def test_check_amazon_fun(self, fun_browser):
        driver = fun_browser
        driver.get('https://www.amazon.com')
        print(driver.title)