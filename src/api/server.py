from datetime import datetime

from flask import Flask

import src.database as mariadb
import mysql.connector.errors as errors

app = Flask(__name__)

db = mariadb.getDbConnection()

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


