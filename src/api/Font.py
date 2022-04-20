from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.fonts.DBFont import DBFont


class Font(Resource):

    def get(self,id):
        json = {}
        try:
            font = DBFont(id)
        except NotFoundException as e:
            abort(e.errorcode)
        json['font'] = font.jsonify()
        return json, 200


