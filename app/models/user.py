from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash

from app.extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)

    author = relationship("Author", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User №{self.id} {self.first_name!r} {self.last_name!r}>"

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
