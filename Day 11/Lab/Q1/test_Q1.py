import pytest

# ----------------------------
# 1. PARAMETRIZE (multiple inputs)
# ----------------------------
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (3, 4, 7),
    (5, 5, 10)
])
def test_addition(a, b, expected):
    assert a + b == expected


# ----------------------------
# 2. SKIP (test will not run)
# ----------------------------
@pytest.mark.skip(reason="Learning skip example")
def test_skip_example():
    assert True


# ----------------------------
# 3. XFAIL (expected to fail)
# ----------------------------
@pytest.mark.xfail(reason="Known issue example")
def test_xfail_example():
    assert False


# ----------------------------
# 4. CUSTOM COMMAND-LINE OPTION
# ----------------------------
import pytest

# STEP 1: Add a command-line option
def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="Guest")


# STEP 2: Read the option in a test
def test_print_name(request):
    name = request.config.getoption("--name")
    print("Hello", name)
    assert name != ""
