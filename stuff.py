def admin():    
    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "admin"},
        {"name": "David"},
        {"name": "Eve", "role": "moderator"}
        ]
    for user in users:
        # if user["role"] == "admin":
        #     print(f"{user['name']} is an admin.")
        try:
            if user["role"] == "admin":
                print(f"{user['name']} is an admin.")
        except KeyError:
            continue
admin()