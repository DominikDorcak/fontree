from flask import request
from flask_restful import Resource, abort

from src import database
from src.api.fonts.DBFontAnswer import DBFontAnswer


class FontAnswer(Resource):

    def post(self):
        json = {}
        req = request.get_json()
        try:
            answer = DBFontAnswer(req["font_answer"])
            answer.save()
            json["font_answer"] = answer.jsonify()
        except Exception:
            db = database.getDbConnection()
            db.close()
            abort(500)

        return json, 201