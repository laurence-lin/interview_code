from schema import Schema
from cerberus import Validator
from datetime import datetime


# Convert string to datetime function
to_date = lambda val: datetime.strptime(val, "%Y-%m-%d")

# Validate rules:
# Missing fields are not allowed
# Empty string are not allowed
# Convert string to integer before validating integer type
data_schema = {
    "ad_network": {"type": "string", "required": True, "empty": False},
    "date": {"type": "date", "required": True, "coerce": to_date},
    "app_name": {"type": "string", "required": True, "empty": False},
    "unit_id": {"type": "integer", "required": True, "coerce": int},
    "request": {"type": "integer", "required": True, "coerce": int},
    "revenue": {"type": "float", "required": True, "coerce": float},
    "imp": {"type": "integer", "required": True, "coerce": int},
}


data = {
    "ad_network": "FOO",
    "date": "2019-06-05",
    "app_name": "LINETV",
    "unit_id": "55665201314",
    "request": "100",
    "revenue": "0.00365325",
    "imp": "23",
}


# error message showed by validator.errors
validator = Validator(data_schema)

result = validator.validate(data)
print(result)
