from flask_combo_jsonapi import ResourceList, ResourceDetail

from app.extensions import db
from app.models import Author
from app.schemas import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author
    }
