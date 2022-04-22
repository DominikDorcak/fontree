from src import database
from src.api.exceptions.NotFoundException import NotFoundException


class DBAnswer:
    def __init__(self, *args):
        if type(args[0]) is int:
            self.id = args[0]
            self.show_value = None
            self.numeric_value = None
            self.question_id = None
            self.load(args[0])
        if type(args[0]) is tuple:
            self.loadDBData(args[0])

    def load(self, id):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM answer WHERE answer_id=%s"
        cursor.execute(sql, [id])
        res = cursor.fetchone()
        if res is None:
            raise NotFoundException
        self.loadDBData(res)

    def loadDBData(self,data):
        self.id = data[0]
        self.question_id = data[1]
        self.show_value = data[2]
        self.numeric_value = int(data[3])

    def jsonify(self):
        return {"answer_id": self.id,
                "question_id": self.question_id,
                "show_value": self.show_value,
                "numeric_value": self.numeric_value}

    @staticmethod
    def loadByQuestionId(question_id):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM answer WHERE question_id=%s"
        cursor.execute(sql,[question_id])
        dbres = cursor.fetchall()
        res = []
        for r in dbres:
            ans = DBAnswer(r)
            res.append(ans)
        return res
