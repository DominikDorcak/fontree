from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.question.DBQuestion import DBQuestion


class AllQuestions(Resource):

    def get(self):
        json = {}
        try:
            questions = DBQuestion.getAll()
        except NotFoundException as e:
            abort(e.errorcode)
        json['questions'] = [q.jsonify() for q in questions]
        return json, 200