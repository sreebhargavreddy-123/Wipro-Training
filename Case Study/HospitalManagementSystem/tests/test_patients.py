import requests
import pytest

def test_get_patients(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200

@pytest.mark.parametrize("name", ["Asha", "Rahul"])
def test_create_patient(base_url, name):
    payload = {
        "name": name,
        "age": 25,
        "gender": "Female",
        "contact": "111",
        "disease": "Flu",
        "doctor": "Dr Rao"
    }
    r = requests.post(base_url, json=payload)
    assert r.status_code == 201

@pytest.mark.skip(reason="Skipping demo")
def test_skip():
    assert False
