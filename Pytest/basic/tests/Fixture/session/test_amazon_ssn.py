from pytest import mark

@mark.ssn_browser
class AmznTest:

    def test_check_amazon_ssn(self, ssn_browser):
        driver = ssn_browser
        driver.get('https://www.amazon.com')
        print(driver.title)