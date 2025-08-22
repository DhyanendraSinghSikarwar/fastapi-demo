# Nested Models Example If i want to apply pydantic validation on address values

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address

address_dict = {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip_code": "12345"
}
address1 = Address(**address_dict)

user_dict = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": address1
}

patient1 = User(**user_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.zip_code)

# Better organization of related data (e.g., vitals, address, insurance)
# Reusability of models across different parts of the application
# Readability and maintainability of code: Nested models make it clear how data is structured and related
# validation: nested models allow for more granular validation of complex data structures