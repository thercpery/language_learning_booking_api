# External imports
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
# Internal imports
from models.User import UserModel
from controllers.users import UserRegister, UserLogin
from db import db

app = Flask(__name__)

app.config["SQL_ALCHEMY_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost/language_learning_booking_app" # postgres database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["JWT_SECRET_KEY"] = "sikretong-malupeeeet"

CORS(app)
db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def init_db():
    UserModel.__table__.create(db.session.bind, checkfirst=True)

@app.route("/")
def index():
    return "Language-Learning Booking App: Learn Any Language Now!"

# routes
api.add_resource(UserRegister, "/api/users/register")
api.add_resource(UserLogin, "/api/users/login")

if __name__ == "__main__":
    app.run()