from ast import arguments
import pytest

class TestSum:
    
    def check_equal(self, a, b):
        print('Checking equality....')
        return a == b

    @pytest.mark.all
    @pytest.mark.parametrize(argnames='num1, num2, error_message', argvalues=[(1, 1, 'Matches'), (1, 2, 'Does Not Match')])
    def test_equal(self, show, num1, num2, error_message):
        # Pass the parameters as the function arguments
        assert self.check_equal(num1, num2), error_message