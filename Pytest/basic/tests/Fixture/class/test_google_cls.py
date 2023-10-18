from pytest import mark

@mark.cls_browser
@mark.usefixtures('cls_browser')
class GoogleTest:

    def test_check_google_1_cls(self):
        driver = self.driver
        driver.get('https://www.google.com')
        print(driver.title)

    def test_check_google_2_cls(self):
        driver = self.driver
        print(driver.title)
        driver.get('https://www.google.com')