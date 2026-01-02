import pytest
from http import HTTPStatus


# include the fixture name as a param in the test function to use it
def test_read_root(client):
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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@example.com',
            }
        ],
    }


def test_read_specific_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'alice updated',
            'email': 'alice_updated@example.com',
            'password': 'test1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alice updated',
        'email': 'alice_updated@example.com',
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'alice updated',
            'email': 'alice_updated@example.com',
            'password': 'test1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alice updated',
        'email': 'alice_updated@example.com',
    }


def test_update_user_fail(client):
    response = client.put(
        '/users/500',
        json={
            'username': 'alice updated',
            'email': 'alice_updated@example.com',
            'password': 'test1234',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user_id not found'}


# Fail test with xfail
@pytest.mark.xfail(reason='user_id not found')
def test_update_user_xfail(client):
    response = client.put(
        '/users/500',
        json={
            'username': 'alice updated',
            'email': 'alice_updated@example.com',
            'password': 'test1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 500,
        'username': 'alice updated',
        'email': 'alice_updated@example.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alice updated',
        'email': 'alice_updated@example.com',
    }
