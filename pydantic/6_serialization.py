# to export the pydantic models
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str = "john.doe@example.com"
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
    "address": address1
}

patient1 = User(**user_dict)

temp = patient1.model_dump_json()  # to export the pydantic models in JSON form
# print(temp)
# print(type(temp))

temp2 = patient1.model_dump()  # to export the pydantic models in dictionary form

# print(temp2)
# print(type(temp2))

temp3 = patient1.model_dump(include={"id", "name"}, exclude={"email", "address"})  # to export the pydantic models in dictionary form with include and exclude
# print(temp3)

temp4 = patient1.model_dump(exclude={"address": {"street", "zip_code"}})  # to export the pydantic models in dictionary form with include and exclude for nested models
# print(temp4)

# since default value of email is present, if we don't want any default value, we want if user provide email only then i should used then we can do it with the help of exclude_unset

temp5 = patient1.model_dump(exclude_unset=True)  # to export the pydantic models in dictionary form with exclude_unset
print(temp5)