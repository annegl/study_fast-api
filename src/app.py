from fastapi import FastAPI
from http import HTTPStatus
from src.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title='Study FastAPI', version='0.1.0')
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {
        'message': 'Hello, you',
        'description': 'This is me learning FastAPI! =)',
    }


# '/': endpoint path (root)

# HTTPStatus:
# 1xx: informational,
# 2xx: success,
# 3xx: redirection,
# 4xx: client error,
# 5xx: server error;
# more on: https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

# response_model:
# specifies the response contract (expected response) for the endpoint
# see contract in src/schemas.py


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        username=user.username,
        email=user.email,
        password=user.password,
        id=len(database) + 1,
    )

    database.append(user_with_id)

    return user_with_id


# response_model returns UserPublic, not UserSchema, to protect password

# model_dump returns a dict of the user's att which can be unpacked into UserDB
# user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
# I don't like the lack of visibility

# breakpoint() # to debug


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}
