from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_root():
    client = TestClient(app)  # Arrange
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'message': 'Hello, you',
        'description': 'This is me learning FastAPI! =)',
    }  # Asset


def test_contact():
    client = TestClient(app)
    response = client.get('/contact/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'contact': 'https://github.com/annegl/'}
