import pytest

# -----------------------------
# Application logic (E2E flow)
# -----------------------------

def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Credentials"

def place_order(is_logged_in, product):
    if is_logged_in and product:
        return "Order Placed"
    return "Order Failed"


# -----------------------------
# Functional Tests
# -----------------------------

def test_successful_order_flow():
    login_status = login("admin", "admin123")
    order_status = place_order(login_status == "Login Successful", "Laptop")
    assert order_status == "Order Placed"


def test_order_without_login():
    order_status = place_order(False, "Laptop")
    assert order_status == "Order Failed"


def test_invalid_login():
    login_status = login("user", "wrong")
    assert login_status == "Invalid Credentials"
