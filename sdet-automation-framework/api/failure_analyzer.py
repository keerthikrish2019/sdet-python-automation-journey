import logging

logger = logging.getLogger(__name__)


def analyze_api_failure(response):

    if response.status_code == 401:
        return "Authentication failure"

    elif response.status_code == 404:
        return "Resource not found"

    elif response.status_code == 500:
        return "Server/database failure"

    else:
        return "Unknown API failure"


def handle_api_failure(response):

    failure_type = analyze_api_failure(response)

    logger.error(
        "API failure: %s, response: %s",
        failure_type,
        response.text
    )

    return failure_type