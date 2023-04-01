from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail
from app.extensions import db
from app.models import Article
from app.schemas import ArticleSchema


class ArticleListEvent(EventsResource):
    def event_get_count(self, *args, **kwargs):
        return {'count': Article.query.count()}


class ArticleDetailEvent(EventsResource):
    def event_get_count_by_author(self, *args, **kwargs):
        return {'count': Article.query.filter(
            Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article
    }
