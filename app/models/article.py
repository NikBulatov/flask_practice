from datetime import datetime
from sqlalchemy import Column, String, Text, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import relationship
from app.extensions import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    created_at = Column(DateTime, default=datetime.utcnow,
                        server_default=func.now())
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    author = relationship("Author", back_populates="articles")
