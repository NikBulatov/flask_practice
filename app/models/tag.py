from sqlalchemy import (Column,
                        String,
                        ForeignKey,
                        Integer,
                        Table)
from sqlalchemy.orm import relationship
from app.extensions import db

article_tag_associations_table = Table(
    "article_tag_associations",
    db.metadata,
    db.Column(
        "article_id", db.Integer, ForeignKey("article.id"), nullable=False),
    db.Column("tag_id", db.Integer, ForeignKey("tag.id"), nullable=False))


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(160), nullable=False, default="", server_default="")

    articles = relationship("Article", secondary=article_tag_associations_table,
                            back_populates="tags")
