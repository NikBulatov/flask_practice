from flask import Blueprint

page = Blueprint(name="page",
                 import_name=__name__,
                 url_prefix="/page",
                 static_folder="../../static")


@page.route("/")
def object_list():
    return "Hello, Page!"


@page.route("/<pk>")
def get_object_item(pk: int):
    return pk
