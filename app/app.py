from flask import Flask, Response

app = Flask(__name__)  # pass file name


@app.route('/')  # register route to run view
def index():  # view
    # return 'Hello World!', 200  # the same way
    return Response('Hello World!', 200)  # data, response status code
