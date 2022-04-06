from db import db

class CourseModel(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String, nullable=False)
    description     = db.Column(db.Text, nullable=False)
    price           = db.Column(db.Float, nullable=False)
    is_active       = db.Column(db.Boolean, default=True)

    def __init__(self, id, name, description, price, is_active):
        self.id             = id
        self.name           = name
        self.description    = description
        self.price          = price
        self.is_active      = is_active

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all_active(cls):
        return cls.query.filter_by(is_active=True).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
