from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class User:

    username: str
    password: str
    phone_number: str
    user_id: str
