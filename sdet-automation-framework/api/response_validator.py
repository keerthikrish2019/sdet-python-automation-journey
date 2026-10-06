import logging

logger = logging.getLogger(__name__)


def validate_user_response(response):
    if response.status_code != 200:
        logger.error(
            "API failed: status=%s, body=%s",
            response.status_code,
            response.text
        )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "email" in data

    return data