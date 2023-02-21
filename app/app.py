from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/')
def index() -> Response:
    return Response('Hello World!')


@app.route('/<string:city>')
def index_city(city: str) -> Response:
    name = request.args.get('name', None)  # get value of query param
    return Response(f'Hello, {city}!')
