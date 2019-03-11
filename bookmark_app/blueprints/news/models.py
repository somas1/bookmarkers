from bookmark_app.extensions import (
    db,
)
from sqlalchemy_searchable import make_searchable, SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from flask_sqlalchemy import BaseQuery

make_searchable()


class PageQuery(BaseQuery, SearchQueryMixin):
    """docstring for PageQuery"""
    pass


class Page(db.Model):
    query_class = PageQuery
    __tablename__ = "pages"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    text = db.Column(db.UnicodeText())
    html = db.Column(db.UnicodeText())
    url = db.Column(db.String(500), unique=True,
                    nullable=False)
    search_vector = db.Column(TSVectorType('text'))

    def __repr__(self):
        """
        Return a string containing a printable
        representation of a Page object.
        ":return: str"
        """
        return 'Title: {}, url: {}'.format(
            unicode(self.title, "utf-8"),
            unicode(self.url, "utf-8")
        )

    @classmethod
    def get_all_entries(cls):
        """
        List all entries saved to database.
        :return: Page object
        """
        return Page.query.all()
