from pytest import mark

@mark.browser
@mark.usefixtures('fun_browser')
class GoogleTest:

    def test_check_google_1_fun(self):
        driver = self.driver
        driver.get('https://www.google.com')
        print(driver.title)

    def test_check_google_2_fun(self):
        driver = self.driver
        print(driver.title)
        driver.get('https://www.google.com')