from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship
from app.db import db


class Article(db.Model):
    title = Column(String(255))
    text = Column(Text())
    authors = relationship('Author')  # 1:N
