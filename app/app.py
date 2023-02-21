from time import time_ns as time
from flask import Flask, Response, g

app = Flask(__name__)


@app.route('/')
def index() -> Response:
    return Response("Hello! In the future something amazing will appear here!")


@app.before_request
def process_before_request() -> None:
    g.start_time = time()


@app.after_request
def process_after_request(response: Response) -> Response:
    if hasattr(g, 'start_time'):
        response.headers['process-time'] = time() - g.start_time
    return response


@app.errorhandler(Exception)
def unknown_url(error) -> Response:
    app.logger.error(error)
    return Response('There is no anything on this site', 404)
