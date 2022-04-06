# External imports
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
# Internal imports
from controllers.users import UserRegister
from db import db

app = Flask(__name__)

app.config["SQL_ALCHEMY_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost/language_learning_booking_app" # postgres database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

CORS(app)
db.init_app(app)
api = Api(app)

@app.before_first_request
def init_db():
    db.create_all()

@app.route("/")
def index():
    return "Language-Learning Booking App: Learn Any Language Now!"

# routes
api.add_resource(UserRegister, "/api/users/register")

if __name__ == "__main__":
    app.run()