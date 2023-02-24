from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
import json

followers = Blueprint(name="followers",
                      import_name=__name__,
                      url_prefix="/followers")


@followers.route("/")
def get_list():
    with open("follower_data.json", "r", encoding="utf-8") as f:
        followers = json.load(f)
        return render_template("followers/list.html", followers=followers)


@followers.route("/<int:pk>")
def get_item(pk: int):
    try:
        with open("follower_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            follower = data[str(pk)]
    except KeyError:
        raise NotFound(f"Follower with ID={pk} not found")
    return render_template("followers/details.html", follower=follower)
