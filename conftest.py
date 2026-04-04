import pytest


@pytest.fixture(scope="session")
def browser():
    print("browser!")

    yield browser

    print("browser closed!")