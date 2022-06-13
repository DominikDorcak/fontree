
from flask import request
from flask_restful import Resource, abort

from src import database
from src.api.experiment.DBEntry import DBEntry


class ExperimentEntry(Resource):

    def post(self):
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
