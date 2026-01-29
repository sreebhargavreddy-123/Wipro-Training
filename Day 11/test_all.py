import pytest
import sys

# --------------------------------------------------
# 1️⃣ Assert Statements and Exceptions
# --------------------------------------------------

# ✅ Simple assert
def test_addition():
    assert 2 + 3 == 5


# ❌ Assert with message
def test_subtraction():
    assert 5 - 3 == 2, "Subtraction result is incorrect"


# 🚨 Exception handling (pytest.raises)
def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# --------------------------------------------------
# 3️⃣ Custom Markers
# --------------------------------------------------

@pytest.mark.smoke
def test_login():
    assert True


# --------------------------------------------------
# 4️⃣ Skips and Expected Failures
# --------------------------------------------------

# ⏭ Skip test
@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment():
    assert True


# ⏭ Conditional skip
@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True


# ⚠ Expected failure
@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 2 * 2 == 5


# --------------------------------------------------
# 7️⃣ Unit Test Example
# --------------------------------------------------

def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(3, 4) == 12


# --------------------------------------------------
# 8️⃣ Functional Test Example
# --------------------------------------------------

def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Credentials"

def test_valid_login():
    assert login("admin", "admin123") == "Login Successful"

def test_invalid_login():
    assert login("user", "wrong") == "Invalid Credentials"
