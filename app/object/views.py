from flask import Blueprint

object_item = Blueprint(name="object",
                        import_name=__name__,
                        url_prefix="/object",
                        static_folder="../../static")


# localhost/object/
@object_item.route("/")
def object_list():
    return "Hello, Object!"


@object_item.route("/<pk>")
def get_object_item(pk: int):
    return pk
