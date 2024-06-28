from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_project.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organizacao)

    response = client.get('/')  # Act (acao)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá Mundo'}  # assert


def test_read_ola_html():
    client = TestClient(app)

    response = client.get('/ola')

    assert response.status_code == HTTPStatus.OK
    assert 'Bem-vindo à Página Elegante' in response.text
    assert 'Esta é uma simples página HTML estilizada.' in response.text
    assert '<h1>' in response.text
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
