from pytest import mark

@mark.ssn_browser
class GoogleTest:

    def test_check_google_1_ssn(self, ssn_browser):
        driver = ssn_browser
        driver.get('https://www.google.com')
        print(driver.title)

    @mark.skip
    def test_check_google_2_ssn(self, ssn_browser):
        driver = ssn_browser
        print(driver.title)
        driver.get('https://www.google.com')