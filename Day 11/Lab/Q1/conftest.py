import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against"
    )

    parser.addini(
        "test_env",
        help="Test environment from pytest.ini",
        default="qa"
    )
