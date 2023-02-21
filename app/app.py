from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index() -> Response:
    return Response('Hello World!')


@app.route('/<string:city>', methods=['GET', 'OPTIONS', 'HEAD'])
def index_city(city: str) -> Response:
    return Response(f'Hello, {city}!')
