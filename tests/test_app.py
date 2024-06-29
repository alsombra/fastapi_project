from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):  # Arrange
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá Mundo'}  # assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testusername',
                'email': 'test@test.com',
            }
        ]
    }


def test_get_read_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }


def test_get_read_user_by_id_deve_retornar_404_0(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_read_user_by_id_deve_retornar_404_1(client):
    response = client.get('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'testusername_alterado',
            'email': 'test@test.com',
            'password': '123',
        },
    )
    assert response.json() == {
        'id': 1,
        'username': 'testusername_alterado',
        'email': 'test@test.com',
    }


def test_update_user_deve_retornar_404(client):
    response = client.put(
        '/users/2',
        json={
            'id': 1,
            'username': 'testusername_alterado2',
            'email': 'test@test.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_deve_retornar_404(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_read_ola_html(client):
    response = client.get('/ola')

    assert response.status_code == HTTPStatus.OK
    assert 'Bem-vindo à Página Elegante' in response.text
    assert 'Esta é uma simples página HTML estilizada.' in response.text
    assert '<h1>' in response.text
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
