from flask_restful import Resource, abort

from src.api.exceptions.NotFoundException import NotFoundException
from src.api.question.DBQuestion import DBQuestion


class AllQuestions(Resource):

    def get(self):
        """
        Vráti zoznam všetkých otázok v json poli
        ---

        responses:
          200:
            description: pole všetkých otázok
            schema:
              id: AllQuestions
              properties:
                questions:
                  type: array
                  items:
                    type: object
                    description: otázka
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
            questions = DBQuestion.getAll()
        except NotFoundException as e:
            abort(e.errorcode)
        json['questions'] = [q.jsonify() for q in questions]
        return json, 200
