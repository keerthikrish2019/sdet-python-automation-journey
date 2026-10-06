from api.failure_analyzer import analyze_api_failure


class FakeResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text


def test_server_failure():
    response = FakeResponse(
        500,
        "Database connection timeout"
    )

    result = analyze_api_failure(response)

    assert result == "Server/database failure"

def test_authentication_failure():
    response = FakeResponse(401, "Unauthorized")

    result = analyze_api_failure(response)

    assert result == "Authentication failure"


def test_resource_not_found():
    response = FakeResponse(404, "User not found")

    result = analyze_api_failure(response)

    assert result == "Resource not found"


def test_unknown_failure():
    response = FakeResponse(400, "Bad request")

    result = analyze_api_failure(response)

    assert result == "Unknown API failure"