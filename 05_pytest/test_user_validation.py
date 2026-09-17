
from sys import path

path.append("01_python_fundamentals")

from user_validation import get_eligible_users


def test_get_eligible_users():
    users = [
        {"name": "John", "age": 35, "active": True},
        {"name": "Mary", "age": 25, "active": True},
        {"name": "Sam", "age": 40, "active": False},
        {"name": "Priya", "age": 32, "active": True},
    ]

    result = get_eligible_users(users)

    assert result == ["John", "Priya"]
