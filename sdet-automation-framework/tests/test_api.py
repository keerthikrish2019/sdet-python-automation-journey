from api.response_validator import validate_user_response
from api.failure_analyzer import handle_api_failure

def test_get_user(api_client):
    response = api_client.get("/users/1")
   
    data = validate_user_response(response)

    assert data["name"] == "Leanne Graham"




def test_api_not_found(api_client):
    response = api_client.get("/users/999")

    assert response.status_code == 404

    failure_type = handle_api_failure(response)

    assert failure_type == "Resource not found"


   
