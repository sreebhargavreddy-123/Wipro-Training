import requests

BASE_URL = "http://127.0.0.1:5000/api/movies"

def test_add_movie():
    payload = {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201


def test_get_movies():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
