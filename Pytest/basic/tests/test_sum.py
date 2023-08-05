import pytest
# import sys
# sys.path.append('..')
from basic.pages.basic import Basic

class TestSum():

    @pytest.mark.sum
    @pytest.mark.positive
    def test_correct_sum(self, show):
        sum = Basic.add_numbers(3, 2)
        assert sum == 5 , 'Correct Value'
        
    @pytest.mark.sum
    @pytest.mark.negative
    def test_incorrect_sum(self):
        sum = Basic.add_numbers(3, 2)
        assert sum == 6, 'Incorrect Value'
