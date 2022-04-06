from flask_restful import Resource, reqparse
from models.User import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("first_name",
        type=str,
        required=True,
        help="Please enter your first name."
    )

    parser.add_argument("last_name",
        type=str,
        required=True,
        help="Please enter your last name."
    )

    parser.add_argument("mobile_number",
        type=str,
        required=True,
        help="Please enter your mobile number."
    )

    parser.add_argument("email",
        type=str,
        required=True,
        help="Please enter your email."
    )

    parser.add_argument("username",
        type=str,
        required=True,
        help="Please enter your username"
    )

    parser.add_argument("password",
        type=str,
        required=True,
        help="Please enter your password"
    )

    parser.add_argument("is_admin",
        type=bool    
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]) and UserModel.find_by_email(data["email"]):
            return False, 400

        if not data["is_admin"]:
            data["is_admin"] = False

        user = UserModel(**data)
        user.save_to_db()

        return True, 201

    