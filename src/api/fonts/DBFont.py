from src import database
from src.api.exceptions.NotFoundException import NotFoundException


class DBFont:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.load(id)

    def load(self, id):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM font WHERE font_id=%s"
        cursor.execute(sql, [id])
        res = cursor.fetchone()
        if res is None:
            raise NotFoundException
        self.id = res[0]
        self.name = res[1]

    @staticmethod
    def getRandomId():
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT font_id FROM font ORDER BY random() LIMIT 1"
        cursor.execute(sql)
        res = cursor.fetchone()
        if res is None:
            raise NotFoundException
        return res[0]




    def jsonify(self):
        return {"font_id": self.id,
                "name": self.name}
