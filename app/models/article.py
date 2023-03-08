from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.extensions import db


class Article(db.Model):
    title = Column(String(255))
    text = Column(Text())
    authors = relationship('Author')  # 1:N
