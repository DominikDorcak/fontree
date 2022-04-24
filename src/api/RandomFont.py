from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.fonts.DBFont import DBFont


class RandomFont(Resource):

    def get(self):
        json = {}
        try:
            font = DBFont.getRandomId()
        except NotFoundException as e:
            abort(e.errorcode)
        json['font_id'] = font
        return json, 200