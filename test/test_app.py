from fastapi.testclient import TestClient
from http import HTTPStatus
from src.app import app

client = TestClient(app)


def test_root():
    client = TestClient(app)  # Arrange
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'message': 'Hello, you',
        'description': 'This is me learning FastAPI! =)',
    }  # Assert


def test_creat_user():
    client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'test123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }
