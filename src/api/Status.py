import os
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
        json['version'] = self.git_version()
        return json, 200

    def git_version(self):
        def _minimal_ext_cmd(cmd):
            # construct minimal environment
            env = {}
            for k in ['SYSTEMROOT', 'PATH']:
                v = os.environ.get(k)
                if v is not None:
                    env[k] = v
            # LANGUAGE is used on win32
            env['LANGUAGE'] = 'C'
            env['LANG'] = 'C'
            env['LC_ALL'] = 'C'
            out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
            return out

        try:
            out = _minimal_ext_cmd(['git', 'describe'])
            GIT_REVISION = out.strip().decode('ascii')
        except OSError:
            GIT_REVISION = "Unknown"

        return GIT_REVISION
