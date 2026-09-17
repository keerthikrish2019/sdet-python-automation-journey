def get_eligible_users(users):
    result = []

    for user in users:
        if user.get("age", 0) >= 30 and user.get("active"):
            result.append(user["name"])

    return result


users = [
    {"name": "John", "age": 35, "active": True},
    {"name": "Mary", "age": 25, "active": True},
    {"name": "Sam", "age": 40, "active": False},
    {"name": "Priya", "age": 32, "active": True},
]

eligible_users = get_eligible_users(users)

print(eligible_users)
