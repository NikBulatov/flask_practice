from flask import Blueprint, render_template

page = Blueprint(name="pages",
                 import_name=__name__,
                 url_prefix="/pages",
                 static_folder="../../static")


@page.route("/")
def pages_list():
    return render_template("pages/list.html", pages=range(5))
