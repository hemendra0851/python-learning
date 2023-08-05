import pytest

@pytest.fixture(params=['1', '2'])
def show(request):
    print(f'start fixture for num {request.param}')
    yield 'number=1'
    print('end fixture')