from flask_combo_jsonapi import ResourceList, ResourceDetail
from app.api.permissions.user import UserListPermission, UserPatchPermission
from app.extensions import db
from app.models import User
from app.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserListPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_patch": [UserPatchPermission],
    }
