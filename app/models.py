from app import db, loginmanager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@loginmanager.user_loader
def load_user(id):
    return db.session.query(Owner).get(int(id))


class Owner(db.Model, UserMixin):
    __tablename__ = 'owners'
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(255), nullable=False)
    apartment = db.Column(db.Integer())
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    role = db.Column(db.Integer(), default=0)
    indicators = db.relationship('Indicator', backref='indicator')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


def reg_owner(login, email, phone_number, apartment, password):
    u = Owner(login=login, email=email, phone_number=phone_number, apartment=apartment)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()


class Indicator(db.Model):
    __tablename__ = 'indicators'
    id = db.Column(db.Integer(), primary_key=True)
    cold = db.Column(db.Integer(), nullable=False)
    hot = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('owners.id'))


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    header = db.Column(db.String(), nullable=False)
    htmltext = db.Column(db.Text())


def create_post(header, htmltext):
    post = Post(header=header, htmltext=htmltext)
    db.session.add(post)
    db.session.commit()


db.create_all()
