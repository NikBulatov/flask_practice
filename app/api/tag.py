from flask_combo_jsonapi import ResourceList, ResourceDetail
from app.extensions import db
from app.models import Tag
from app.schemas import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }
