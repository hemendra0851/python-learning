from pytest import mark
from basic.pages.basic import Basic

@mark.prod
class TestProd():
    
    @mark.positive
    # @mark.skipif
    def test_correct_prod(self):
        prod = Basic.multiply_numbers(3, 2)
        assert prod == 6 , 'Correct Value'
    
    @mark.negative
    def test_incorrect_prod(self):
        prod = Basic.multiply_numbers(3, 2)
        assert prod == 5, 'Incorrect Value'