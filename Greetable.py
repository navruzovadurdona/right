from typing import Protocol

class Greetable(Protocol):
    def greet(self) -> str:
        """Return a greeting message."""
        pass

class Person:

    def greet(self) -> str:
        return "Hello, world!"
    
class Animal:

    def greet (self) -> str:
        return "Hi!"
    
def greet_entity(entity: Greetable) -> str:
    """Greet the entity."""
    return entity.greet()

person = Person()
animal = Animal()

print(greet_entity(person))  # Output: Hello, world!
print(greet_entity(animal))  # Output: Hi!




from typing import NewType

UserID = NewType('UserID', int)
ProductID = NewType('ProductID', int)

def get_user(user_id: UserID) -> str:
    return f"User  with ID: {user_id}"
user_id = UserID(21345465432376)
print(get_user(user_id))  # Output: User with ID: 21345465432376


product_id = ProductID(123456789)
print(get_user(product_id))  # Output: User with ID: 123456789



from typing import Final

PI: Final = 3.14



from typing import Final
from fastapi import FastAPI


app = FastAPI()

class User(TypedDict):
    name: str
    age: int

@app.post("/creat_user/")
async def create_user(user: User) -> str:
    return f"User {user['name']} with age {user['age']} created successfully!"

@app.get("/get_user/")
async def get_user() -> list[User]:
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 28},
        {"name": "Eve", "age": 22},
        {"name": "Frank", "age": 40},
        {"name": "Grace", "age": 27},
        {"name": "Heidi", "age": 32},
        {"name": "Ivan", "age": 29},
        {"name": "Judy", "age": 31},
    ]
print(get_user())
