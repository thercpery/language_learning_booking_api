from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.Course import CourseModel

class AddCourse(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument("description",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument("price",
        type=float,
        required=True,
        help="This field cannot be blank"
    )

    @jwt_required()
    def post(self):
        data = AddCourse.parser.parse_args()
        if CourseModel.find_by_name(data["name"]):
            return False, 400

        course = CourseModel(**data, is_active=True)
        course.save_to_db()

        return True, 201

class CoursesList(Resource):
    def get(cls):
        return [course.json() for course in CourseModel.find_all_active()]
