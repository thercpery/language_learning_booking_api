from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from werkzeug.security import generate_password_hash, check_password_hash, safe_str_cmp
from models.User import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument("username",
    type=str,
    required=True,
    help="Username is required"
)

_user_parser.add_argument("password",
    type=str,
    required=True,
    help="Username is required"
)


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
            # If there is an existing username or email.
            return False, 400

        if not data["is_admin"]:
            # If is_admin is not indicated
            data["is_admin"] = False

        # Encrypt password
        data["password"] = generate_password_hash(data["password"], salt_length=10)

        user = UserModel(**data)
        user.save_to_db()

        return True, 201

    
class UserLogin(Resource):
    @classmethod
    def post(cls):
        """ 
            This authenticates the user manually
            1. Get the data from parser(request body).
            2. Find the user in the database.
            3. Check the password.
            4. Create an access token.
            5. Craete refresh token (will look at this later).
            6. Return the access token
        """
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data["username"])
        password = generate_password_hash(data["password"], salt_length=10)
        print(check_password_hash(user.password, data["password"]))
        if user and check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)

            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200

        return False, 401
