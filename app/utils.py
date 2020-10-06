from flask import make_response
from app import db
from app.models import Owner


def cookies():
    res = make_response("")
    user_id = db.session.query(Owner).get(int(id))
    res.set_cookie("id", user_id, 60 * 60 * 24 * 15)
