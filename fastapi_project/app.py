from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastapi_project.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


def get_by_id(database, id):
    for user in database:
        if user.id == id:
            return user
    return None


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail='User not found')

    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user_by_id(user_id: int):
    user = get_by_id(database, user_id)

    if user_id < 1 or user_id > len(database) or user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail='User not found')

    del database[user_id - 1]

    return {'message': 'User deleted'}


@app.get('/ola', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_ola_html():
    my_html_response = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página Elegante</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f0f0f0;
                color: #333;
                text-align: center;
            }
            h1 {
                color: #0366d6;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                display: inline-block;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bem-vindo à Página Elegante</h1>
            <p>Esta é uma simples página HTML estilizada.</p>
            <p>by Antonio Luis Sombra de Medeiros</p>
        </div>
    </body>
    </html>"""
    return HTMLResponse(my_html_response)
