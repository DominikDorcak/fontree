from datetime import datetime

from flask_restful import Resource, abort
from src import database


class Status(Resource):

    def get(self):
        db = database.getDbConnection()
        c = db.cursor()
        online = True
        json = {}
        try:
            starttime = datetime.now()
            c.execute('SELECT version()')
            res = c.fetchone()
            time = datetime.now() - starttime
        except Exception:
            online = False

        json['db'] = {"online":online,
                      "version": res[0],
                      "ping": str(time.total_seconds() * 1000) + "ms" if online else None,}
        return json, 200
