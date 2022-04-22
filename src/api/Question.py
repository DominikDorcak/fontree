from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.question.DBQuestion import DBQuestion


class Question(Resource):

    def get(self,id):
        json = {}
        try:
            question = DBQuestion(id)
        except NotFoundException as e:
            abort(e.errorcode)
        json['question'] = question.jsonify()
        return json, 200


