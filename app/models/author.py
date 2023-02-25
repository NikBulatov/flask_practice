from sqlalchemy import Column, Integer, String, Boolean
from app.db import db


class Author(db.Model):
    id = Column(Integer, primary_key=True)
    password = Column(String(255), unique=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
