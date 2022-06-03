import subprocess
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
        json['status'] = 'online'
        json['version'] = 'git-' + self.get_git_revision_short_hash()
        return json, 200

    def get_git_revision_short_hash(self) -> str:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
