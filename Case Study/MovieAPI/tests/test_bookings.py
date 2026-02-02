import requests

MOVIES_URL = "http://127.0.0.1:5000/api/movies"
BOOKING_URL = "http://127.0.0.1:5000/api/bookings"


def test_book_ticket():
    # Step 1: Add movie first
    movie_payload = {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
    requests.post(MOVIES_URL, json=movie_payload)

    # Step 2: Book ticket
    booking_payload = {
        "movie_id": 101,
        "seats": 2
    }
    response = requests.post(BOOKING_URL, json=booking_payload)

    # Step 3: Assertion
    assert response.status_code == 201
    assert response.json()["total_price"] == 500
