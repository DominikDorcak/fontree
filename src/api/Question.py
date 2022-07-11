from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.question.DBQuestion import DBQuestion


class Question(Resource):

    def get(self,id):
        """
                        Načítanie údajov o otázke
                ---
                        parameters:
                          - in: path
                            name: id
                            type: integer
                            required: true
                        responses:
                          200:
                            description: Otázka
                            schema:
                              id: Question
                              properties:
                                question:
                                  type: object
                                  properties:
                                    question_id:
                                      type: integer
                                      description: ID otázky
                                    text:
                                      type: string
                                      description: znenie otázky
                                    answers:
                                      type: array
                                      items:
                                        type: object
                                        description: odpoveď na otázku
                                        properties:
                                          question_id:
                                            type: integer
                                            description: ID otázky
                                          answer_id:
                                            type: integer
                                            description: ID odpovede
                                          numeric_value:
                                            type: integer
                                            description: číselná hodnota odpovede
                                          show_value:
                                            type: string
                                            description: textová hodnota odpovede
                                            default: nie
                        """

        json = {}
        try:
            question = DBQuestion(id)
        except NotFoundException as e:
            abort(e.errorcode)
        json['question'] = question.jsonify()
        return json, 200


