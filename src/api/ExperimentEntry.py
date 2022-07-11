
from flask import request
from flask_restful import Resource, abort

from src import database
from src.api.experiment.DBEntry import DBEntry


class ExperimentEntry(Resource):

    def post(self):
        """
                                pridať príspevok do experimentu
                                ---
                                parameters:
                                  - name: body
                                    in: body
                                    description: Dáta príspevku
                                    required: true
                                    schema:
                                      id: Entry
                                      properties:
                                        entry:
                                          type: object
                                          description: data
                                          properties:
                                            age:
                                              type: integer
                                            sex:
                                              type: string
                                            highest_education:
                                              type: integer
                                            asigned_font:
                                              type: integer
                                            result_font:
                                              type: integer
                                            time_in_milis:
                                              type: integer
                                            question_count:
                                              type: integer

                                responses:
                                  201:
                                    description: objekt s id a časom pridaného príspevku
                                    schema:
                                      id: Inserted
                                      properties:
                                        inserted:
                                          type: object
                                          properties:
                                            id:
                                              type: integer
                                            entry_time:
                                              type: string

                        """

        json = {}
        req = request.get_json()
        try:
            dbentry = DBEntry(req["entry"])
            dbentry.save()
            json["inserted"] = {
                "id": dbentry.id,
                "entry_time": dbentry.entry_time.isoformat()
            }
        except Exception:
            db = database.getDbConnection()
            db.close()
            abort(500)

        return json, 201

    def get(self):
        """
                        Všetky príspevky do experimentu
                        ---

                        responses:
                          200:
                            description: pole príspevkov do experimentu
                            schema:
                              id: Entries
                              properties:
                                entries:
                                  type: array
                                  description: pole príspevkov do experimentu
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: integer
                                      age:
                                        type: integer
                                      sex:
                                        type: string
                                      highest_education:
                                        type: integer
                                      asigned_font:
                                        type: integer
                                      result_font:
                                        type: integer
                                      time_in_milis:
                                        type: integer
                                      question_count:
                                        type: integer
                                      entry_time:
                                        type: string
                """

        json = {}
        entires = DBEntry.getall()
        json['entries'] = entires
        return json, 200