from pytest import mark

class TestParam:
    
    def check_equal(self, a, b):
        print('Checking equality....')
        return a == b

    @mark.all
    @mark.parametrize(argnames='num1, num2, error_message', argvalues=[(1, 1, 'Matches'), (1, 2, 'Does Not Match')])
    def test_equal(self, num1, num2, error_message):
        # Pass the parameters as the function arguments
        # print(show)
        assert self.check_equal(num1, num2), error_message