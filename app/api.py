from flask_restx import Api
from flask_restx import fields, Resource
from app.models import Tag, User, Article, Author

__all__ = ["api", ]

api = Api(version='1.0', title='App API',
          description='A simple App API',
          doc="/api/swagger/", ordered=True)

TAG_SCHEMA = api.model("Tag", {
    "id": fields.Integer(description="Tag ID"),
    "name": fields.String(description="Tag name"),
})

AUTHOR_SCHEMA = api.model("Author", {
    "id": fields.Integer(description="Author ID"),
    "user_id": fields.Integer(description="User ID")
})

ARTICLE_SCHEMA = api.model("Article", {
    "id": fields.Integer(description="Article ID"),
    "title": fields.String(description="Article title"),
    "body": fields.String(description="Article content"),
    "author_id": fields.Integer(description="Author ID"),
    "created_at": fields.DateTime(description="Datetime created"),
    "updated_at": fields.DateTime(description="Datetime updated")
})

USER_SCHEMA = api.model("User", {
    "id": fields.Integer(description="User ID"),
    "first_name": fields.String(description="User first name"),
    "last_name": fields.String(description="User last name"),
    "is_staff": fields.Boolean(description="User permissions")
})


@api.route("/api/tags/")
@api.doc()
class TagList(Resource):
    @api.marshal_list_with(TAG_SCHEMA)
    def get(self):
        return Tag.query.all()


@api.route("/api/tags/<string:id>")
@api.doc()
class TagDetail(Resource):
    @api.marshal_with(TAG_SCHEMA)
    def get(self, id):
        return Tag.query.get_or_404(id)


@api.route("/api/users/")
@api.doc()
class UserList(Resource):
    @api.marshal_list_with(USER_SCHEMA)
    def get(self):
        return User.query.all()


@api.route("/api/users/<int:id>")
@api.doc()
class UserDetail(Resource):
    @api.marshal_with(USER_SCHEMA)
    def get(self, id):
        return User.query.get_or_404(id)


@api.route("/api/articles/")
@api.doc()
class ArticleList(Resource):
    @api.marshal_list_with(ARTICLE_SCHEMA)
    def get(self):
        return Article.query.all()


@api.route("/api/articles/<int:id>")
@api.doc()
class ArticleDetail(Resource):
    @api.marshal_with(ARTICLE_SCHEMA)
    def get(self, id):
        return Article.query.get_or_404(id)


@api.route("/api/authors/")
@api.doc()
class AuthorList(Resource):
    @api.marshal_list_with(AUTHOR_SCHEMA)
    def get(self):
        return Author.query.all()


@api.route("/api/authors/<int:id>")
@api.doc()
class AuthorDetails(Resource):
    @api.marshal_with(AUTHOR_SCHEMA)
    def get(self, id):
        return Author.query.get_or_404(id)
