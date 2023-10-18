from pytest import mark

@mark.cls_browser
class AmznTest:

    def test_check_amazon_cls(self, cls_browser):
        driver = cls_browser
        driver.get('https://www.amazon.com')
        print(driver.title)