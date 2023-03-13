import pydantic


class HttpError(Exception):
    def __init__(self, status_code: int, description: str | dict | list):
        self.status_code = status_code
        self.description = description


def validate(input_data: dict, validation_model):
    try:
        model_item = validation_model(**input_data)
        return model_item.dict()
    except pydantic.ValidationError as err:
        raise HttpError(400, err.errors())


class CreateUser(pydantic.BaseModel):
    email: str
    password: str

    @pydantic.validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError(f'password is too short: len = {len(value)}. Necessary min len = 8')
        return value

