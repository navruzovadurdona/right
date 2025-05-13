from typing import NewType

UserID = NewType('UserID', int)
ProductID = NewType('ProductID', int)

def get_user(user_id: UserID) -> str:
    return f"User  with ID: {user_id}"
user_id = UserID(21345465432376)
print(get_user(user_id))  # Output: User with ID: 21345465432376


product_id = ProductID(123456789)
print(get_user(product_id))  # Output: User with ID: 123456789
