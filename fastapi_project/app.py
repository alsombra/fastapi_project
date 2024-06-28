from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_project.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


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
