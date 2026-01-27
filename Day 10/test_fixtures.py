import pytest

@pytest.fixture
def data():
    return [1,2,3]

def test_one(data):          # <- fixture used here
    assert 2 in data

def test_two(data):          # <- fixture used here
    assert len(data) == 3
