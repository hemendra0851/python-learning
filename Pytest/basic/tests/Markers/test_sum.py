from pytest import mark
from basic.pages.basic import Basic

# @mark.usefixtures('show')
class TestSum():

    @mark.sum
    @mark.positive
    def test_correct_sum(self):
        sum = Basic.add_numbers(3, 2)
        assert sum == 5 , 'Correct Value'
        
    @mark.sum
    @mark.negative
    def test_incorrect_sum(self):
        sum = Basic.add_numbers(3, 2)
        assert sum == 6, 'Incorrect Value'
