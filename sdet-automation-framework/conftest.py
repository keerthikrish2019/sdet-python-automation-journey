import pytest

from api.api_client import APIClient
from config import BASE_URL, TOKEN


@pytest.fixture
def api_client():
    return APIClient(BASE_URL, TOKEN)