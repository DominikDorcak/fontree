from datetime import datetime

import yaml
from flask import Flask
from flask_restful import Api


import src.database as mariadb
import mysql.connector.errors as errors

from src.api.Font import Font
from src.api.Image import Image
from src.api.Node import Node

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from src import config

app = Flask(__name__)
cfg = yaml.safe_load(pkg_resources.read_text(config, 'config.yaml'))
db = mariadb.getDbConnection()

api = Api(app)
api.add_resource(Image, '/image/<path:path>')
api.add_resource(Node, '/node/<int:id>')
api.add_resource(Font, '/font/<int:id>')



@app.route("/status")

def status():
    res = db.get_server_info()
    online = True
    try:
        starttime = datetime.now()
        ping = db.ping(reconnect=True,attempts=2,delay=1)
        time = datetime.now()-starttime
    except errors.InterfaceError:
        online = False

    db_status = ("online: " + res + " ping:" + str(time.total_seconds() * 1000) + "ms") if online else "offline"
    return """<!DOCTYPE html>
        <html>
            <head>
                <title>Status</title>
            </head>
        <body> 
        <H2> API ONLINE</H2>
        <p> Database: """ + db_status + """</body>
        </html>"""


