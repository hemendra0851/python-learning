import pytest
from basic.pages.basic import Basic

class TestProd():
    
    @pytest.mark.prod
    @pytest.mark.positive
    def test_correct_prod(self):
        prod = Basic.multiply_numbers(3, 2)
        assert prod == 6 , 'Correct Value'
    
    @pytest.mark.prod
    @pytest.mark.negative
    def test_incorrect_prod(self):
        prod = Basic.multiply_numbers(3, 2)
        assert prod == 5, 'Incorrect Value'