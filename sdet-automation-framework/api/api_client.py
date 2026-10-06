import logging
import requests

logger = logging.getLogger(__name__)


class APIClient:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get(self, endpoint):
        logger.info(f"GET request: {endpoint}")

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=headers
        )

        logger.info(f"Response status: {response.status_code}")

        return response