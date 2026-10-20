import pytest

@pytest.fixture(scope="session")
def practice_url(base_url):
    return base_url