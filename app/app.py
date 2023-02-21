from time import time

from flask import Flask, Response, g

app = Flask(__name__)


@app.route('/')
def index() -> Response:
    return Response('Hello World!')


@app.route('/<string:city>')
def index_city(city: str) -> Response:
    return Response(f'Hello, {city}!')


@app.before_request
def process_before_request() -> None:
    g.start_time = time()


@app.after_request
def process_after_request(response: Response) -> Response:
    if hasattr(g, 'start_time'):
        response.headers['process-time'] = time() - g.start_time
    return response


@app.errorhandler(404)  # or pass Exception class
def fatal_404(error) -> Response:
    app.logger.error(error)
    return Response('Bad request', 404)
