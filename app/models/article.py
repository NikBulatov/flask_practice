from datetime import datetime
from sqlalchemy import Column, String, Text, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import relationship
from app.extensions import db
from app.models.tag import article_tag_associations_table


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    created_at = Column(DateTime, default=datetime.utcnow,
                        server_default=func.now())
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    author = relationship("Author", back_populates="articles")
    tags = relationship("Tag", secondary=article_tag_associations_table,
                        back_populates="articles")

    def __str__(self):
        return self.title
