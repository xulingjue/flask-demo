from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import event, DDL

# 全局数据库访问对象
db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.name)


class UserBase(Base, UserMixin):
    __abstract__ = True

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    email = db.Column(db.String(64), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(128), nullable=False)
    is_enable = db.Column(db.Boolean, default=True, index=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def is_user(self):
        return self.role == self.ROLE_USER

    def is_company(self):
        return self.role == self.ROLE_COMPANY

    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def check_password(self, password):
        return check_password_hash(self._password, password)


class User(UserBase):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(8), nullable=False)
    resume = db.Column(db.String(128))
    role = db.Column(db.SmallInteger, default=UserBase.ROLE_USER)


event.listen(User.__table__, "after_create", DDL("ALTER TABLE user AUTO_INCREMENT = 100000000"))
