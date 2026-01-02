from http import HTTPStatus

from fastapi import FastAPI

from src.schemas import Contact, Message

app = FastAPI(title='Study FastAPI', version='0.1.0')


@app.get(
    '/',  # root path
    status_code=HTTPStatus.OK,
    # 1xx: informational,
    # 2xx: success,
    # 3xx: redirection,
    # 4xx: client error,
    # 5xx: server error;
    # more on: https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
    response_model=Message,  # see contract in src/schemas.py
)
def read_root():
    return {
        'message': 'Hello, you',
        'description': 'This is me learning FastAPI! =)',
    }


@app.get('/contact/', status_code=HTTPStatus.OK, response_model=Contact)
def read_contact():
    return {'contact': 'https://github.com/annegl/'}
