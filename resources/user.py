from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='this field is required')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='this field is required')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': f'a user already exists with username {data["username"]}'}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'user created successfully'}, 201
