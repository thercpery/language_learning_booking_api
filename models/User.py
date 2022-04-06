from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id              = db.Column(db.Integer, primary_key=True)
    first_name      = db.Column(db.String(100), nullable=False)
    last_name       = db.Column(db.String(100), nullable=False)
    mobile_number   = db.Column(db.String(50), nullable=False)
    email           = db.Column(db.String(100), nullable=False)
    username        = db.Column(db.String(100), nullable=False)
    password        = db.Column(db.String(100), nullable=False)
    is_admin        = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, mobile_number, email, username, password, is_admin):
        self.first_name     = first_name
        self.last_name      = last_name
        self.mobile_number  = mobile_number
        self.email          = email
        self.username       = username
        self.password       = password
        self.is_admin       = is_admin

    def json(self):
        return {
            "id": self.id,
            "name": f"{self.first_name} {self.last_name}",
            "mobile_number": self.mobile_number,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin 
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()