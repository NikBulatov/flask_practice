from flask import Blueprint, render_template

object_item = Blueprint(name="objects",
                        import_name=__name__,
                        url_prefix="/objects",
                        static_folder="../../static")

OBJECTS = ("Apple", "Phone", "Book")


# localhost/object/
@object_item.route("/")
def object_list():
    context = {
        "objects": OBJECTS
    }
    return render_template("objects/list.html", **context)


@object_item.route("/<int:pk>")
def get_object_item(pk: int):
    return str(pk)
