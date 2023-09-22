import re
from fastapi import HTTPException, status
from pydantic import BaseModel, constr, root_validator


class UserIn(BaseModel):
    userName: str
    fullName: str
    email: str
    hashedPassword: str
    DoB: constr(pattern=r'^\d{2}-\d{2}-\d{4}$')
    gender: str

    @root_validator(skip_on_failure=True)
    def validate_fields(cls, values):
        errors = {}

        if not values['userName'].isalpha():
            errors['userName'] = "Enter Just Characters For userName"

        if not values['fullName'].isalpha():
            errors['fullName'] = "Enter Just Characters For fullName"

        if "@" not in values['email']:
            errors['email'] = "Email Must Have @"

        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z]).*$", values["hashedPassword"]):
            errors["hashedPassword"] = "The Password Must Uppercase And Lowercase"

        if not re.match(r'^\d{2}-\d{2}-\d{4}$', values["DoB"]):
            errors["DoB"] = "Invalid date of birth format. Use mm-dd-yyyy."

        if values["gender"] not in ["Male", "Female"]:
            errors["gender"] = "The gender Must Be Male Or Female"
        if errors:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"detail": errors})

        return values


class UserCh(BaseModel):
    email: str