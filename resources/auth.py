from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from schemas.request_schemas.users import UserSignUpRequestSchema, UserSignInRequestSchema
from schemas.response_schemas.users import UserAuthResponseSchema
from utils.decorators import validate_schema


class SignUpResource(Resource):
    @validate_schema(UserSignUpRequestSchema)
    def post(self):
        data = request.get_json()
        user = AuthManager.create_user(data)
        token = AuthManager.encode_token(user)
        return UserAuthResponseSchema().dump({"token": token})

class SignInResource(Resource):
    @validate_schema(UserSignInRequestSchema)
    def post(self):
        data = request.get_json()
        user = AuthManager.sign_in_user(data)

        token = AuthManager.encode_token(user)
        return UserAuthResponseSchema().dump({"token": token})
