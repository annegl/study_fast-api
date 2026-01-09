from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from src.models import User
from src.schemas import Message, UserPublic, UserSchema
from src.settings import Settings

app = FastAPI(title='Study FastAPI', version='0.1.0')

engine = create_engine(
    Settings().DATABASE_URL
)  # Database engine: manages the low-level connection to the DB.
session = Session(
    engine
)  # ORM session: manages Python objects and translates them into SQL.


def check_user_exists(user: UserSchema):
    return session.scalar(
        select(User).where(
            User.username == user.username, User.email == user.email
        )
    )


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
# response_model returns UserPublic, not UserSchema, to protect password
def create_user(user: UserSchema):
    if check_user_exists(user):
        session.close()
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='User name or e-mail already exist',
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
    )

    try:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()


# breakpoint() # to debug

# TODO: Update this logict
# @app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
# def read_users():
#     return {'users': database}


# @app.put(
#     '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
# )
# def update_user(user_id: int, user: UserSchema):
#     check_user_exists(user_id)
#     user_with_id = UserDB(**user.model_dump(), id=user_id)
#     database[user_id - 1] = user_with_id
#     return user_with_id


# @app.get('/users/{user_id}', response_model=UserPublic)
# def get_user(user_id: int):
#     check_user_exists(user_id)
#     return database[user_id - 1]


# @app.delete(
#     '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
# )
# def delete_user(user_id: int):
#     check_user_exists(user_id)
#     return database.pop(user_id - 1)
