from http import HTTPStatus


# include the fixture name as a param in the test function to use it
def test_root(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'message': 'Hello, you',
        'description': 'This is me learning FastAPI! =)',
    }  # Assert


def test_creat_user(client):
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
