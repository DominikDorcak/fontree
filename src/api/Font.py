from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.fonts.DBFont import DBFont


class Font(Resource):

    def get(self,id):
        """
                Načítanie údajov o fonte
        ---
                parameters:
                  - in: path
                    name: id
                    type: integer
                    required: true
                responses:
                  200:
                    description: Font
                    schema:
                      id: Font
                      properties:
                        font:
                          type: object
                          properties:
                            font_id:
                              type: integer
                              description: ID fontu
                            name:
                              type: string
                              description: meno fontu
                              default: Arial
                """
        json = {}
        try:
            font = DBFont(id)
        except NotFoundException as e:
            abort(e.errorcode)
        json['font'] = font.jsonify()
        return json, 200


