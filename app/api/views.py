from flask import request
from app import db
from app.models import Owner, Post, Indicator
from . import api

# Запросы с методом PUT
@api.route('/post/<int:id>', methods=['PUT'])
def change_post(id):
    data = request.get_json(force=True)
    db.session.query(Post).filter_by(id=id).update(data)
    db.session.commit()
    return 'ok', 200

@api.route('/owner/<int:id>', methods=['PUT'])
def change_owner(id):
    data = request.get_json(force=True)
    db.session.query(Owner).filter_by(id=id).update(data)
    db.session.commit()
    return 'ok', 200


@api.route('/indicator/<int:id>', methods=['PUT'])
def change_ind(id):
    data = request.get_json(force=True)
    db.session.query(Indicator).filter_by(id=id).update(data)
    db.session.commit()
    return 'ok', 200

#Запросы с методом DELETE
@api.route('/post/<int:id>', methods=['DELETE'])
def del_post(id):
    db.session.query(Post).filter_by(id=id).delete()
    db.session.commit()
    return '', 200


@api.route('/owner/<int:id>', methods=['DELETE'])
def del_owner(id):
    db.session.query(Owner).filter_by(id=id).delete()
    db.session.commit()
    return '', 200


@api.route('/indicator/<int:id>', methods=['DELETE'])
def del_ind(id):
    db.session.query(Indicator).filter_by(id=id).delete()
    db.session.commit()
    return '', 200
