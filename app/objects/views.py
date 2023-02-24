from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

object_item = Blueprint(name="objects",
                        import_name=__name__,
                        url_prefix="/objects",
                        static_folder="../../static")

OBJECTS = {1: "Apple", 2: "Phone", 3: "Book"}


@object_item.route("/")
def object_list():
    return render_template("objects/list.html", objects=OBJECTS)


@object_item.route("/<int:pk>")
def get_object_item(pk: int):
    try:
        object_inst = OBJECTS[pk]
    except KeyError:
        raise NotFound(f"Object ID {pk} not found")
        # or redirect("/objects/")
    return render_template("objects/details.html", object_inst=object_inst)
