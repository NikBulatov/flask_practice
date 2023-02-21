from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/')
def index() -> Response:
    return Response('Hello World!')


@app.route('/<string:city>')
def index_city(city: str) -> Response:
    return Response(f'Hello, {city}!')
