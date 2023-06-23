
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


def connect_db(app):
    """Connect this db to provided Flask app"""
    db.app = app
    db.init_app(app)


"""Models for Blogly."""


class User(db.Model):
    __tablename__ = 'users'

    def _repr_(self):
        u = self
        return f"<user id=(u.id) first_name=(u.firstname) last_name=(u.lastname) image_url=(u.imageurl)>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.Text,
                           nullable=False,
                           unique=True)

    last_name = db.Column(db.Text,
                          nullable=False,
                          unique=True)

    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)


    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")


    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"



class Post(db.Model):
    """Blog post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
