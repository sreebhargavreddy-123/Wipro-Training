import pytest
import sys

# --------------------------------------------------
# 1️⃣ Parameterized Tests
# --------------------------------------------------

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0)
])
def test_addition(a, b, expected):
    assert a + b == expected


# --------------------------------------------------
# 2️⃣ Read Configuration from pytest.ini
# --------------------------------------------------

def test_read_ini_config(pytestconfig):
    env = pytestconfig.getini("test_env")
    assert env in ["dev", "qa", "prod"]


# --------------------------------------------------
# 3️⃣ Use Custom CLI Option
# --------------------------------------------------

def test_command_line_option(request):
    env = request.config.getoption("env")
    assert env in ["dev", "qa", "prod"]


# --------------------------------------------------
# 4️⃣ Skips and Expected Failures
# --------------------------------------------------

@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment():
    assert True


@pytest.mark.skipif(sys.platform == "win32", reason="Linux-only feature")
def test_linux_only():
    assert True


@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 2 * 2 == 5


def pytest_addoption(parser):
    # Register custom CLI option
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests"
    )

    # Register pytest.ini config value
    parser.addini(
        "test_env",
        help="Test environment from pytest.ini",
        default="qa"
    )