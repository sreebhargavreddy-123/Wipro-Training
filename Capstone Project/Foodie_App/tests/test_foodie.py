import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ===============================
# RESTAURANT TESTS
# ===============================

def test_01_register_restaurant(client):
    res = client.post("/api/v1/restaurants", json={
        "name": "Food Palace",
        "contact": "9999999999",
        "images": ["img.jpg"]
    })
    assert res.status_code == 201


def test_02_view_restaurant(client):
    res = client.get("/api/v1/restaurants/1")
    assert res.status_code == 200


def test_03_update_restaurant(client):
    res = client.put("/api/v1/restaurants/1", json={"location": "Hyderabad"})
    assert res.status_code == 200


def test_04_disable_restaurant(client):
    res = client.put("/api/v1/restaurants/1/disable")
    assert res.status_code == 200


# ===============================
# DISH TESTS
# ===============================

def test_05_add_dish(client):
    # Re-enable restaurant
    client.put("/api/v1/admin/restaurants/1/approve")

    res = client.post("/api/v1/restaurants/1/dishes", json={
        "name": "Biryani",
        "type": "Veg",
        "price": 200,
        "available_time": "Lunch",
        "image": "bir.jpg"
    })
    assert res.status_code == 201


def test_06_update_dish(client):
    res = client.put("/api/v1/dishes/1", json={"price": 250})
    assert res.status_code == 200


def test_07_dish_status(client):
    res = client.put("/api/v1/dishes/1/status", json={"enabled": False})
    assert res.status_code == 200


def test_08_delete_dish(client):
    res = client.delete("/api/v1/dishes/1")
    assert res.status_code == 200


# ===============================
# USER TESTS
# ===============================

def test_09_register_user(client):
    res = client.post("/api/v1/users/register", json={
        "name": "John",
        "email": "john@test.com",
        "password": "123"
    })
    assert res.status_code == 201


# ===============================
# SEARCH
# ===============================

def test_10_search(client):
    res = client.get("/api/v1/restaurants/search")
    assert res.status_code == 200


# ===============================
# ORDER FLOW
# ===============================

def test_11_place_order(client):
    # Reactivate restaurant (was disabled in earlier test)
    client.put("/api/v1/restaurants/1", json={"active": True})

    # Approve restaurant
    client.put("/api/v1/admin/restaurants/1/approve")

    # Add dish and capture ID
    dish_res = client.post("/api/v1/restaurants/1/dishes", json={
        "name": "Pizza",
        "type": "Veg",
        "price": 300,
        "available_time": "Dinner",
        "image": "p.jpg"
    })

    dish_id = dish_res.get_json()["id"]

    order_res = client.post("/api/v1/orders", json={
        "user_id": 1,
        "restaurant_id": 1,
        "dishes": [dish_id]
    })

    assert order_res.status_code == 201

    global ORDER_ID
    ORDER_ID = order_res.get_json()["id"]


def test_12_orders_by_restaurant(client):
    res = client.get("/api/v1/restaurants/1/orders")
    assert res.status_code == 200


def test_13_orders_by_user(client):
    res = client.get("/api/v1/users/1/orders")
    assert res.status_code == 200


# ===============================
# RATING
# ===============================

def test_14_rating(client):
    res = client.post("/api/v1/ratings", json={
        "order_id": ORDER_ID,
        "rating": 5,
        "comment": "Good"
    })
    assert res.status_code == 201


# ===============================
# ADMIN
# ===============================

def test_15_admin_approve(client):
    res = client.put("/api/v1/admin/restaurants/1/approve")
    assert res.status_code == 200


def test_16_admin_disable(client):
    res = client.put("/api/v1/admin/restaurants/1/disable")
    assert res.status_code == 200


def test_17_admin_feedback(client):
    res = client.get("/api/v1/admin/feedback")
    assert res.status_code == 200


def test_18_admin_orders(client):
    res = client.get("/api/v1/admin/orders")
    assert res.status_code == 200