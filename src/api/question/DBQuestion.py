from src import database
from src.api.exceptions.NotFoundException import NotFoundException
from src.api.question.DBAnswer import DBAnswer


class DBQuestion:
    def __init__(self, *args):
        self.text = None
        self.answers = []
        self.id = None
        if len(args) == 1 and type(args[0]) is int:
            self.id = args[0]
            self.load(self.id)

    def load(self, id):
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM question WHERE question_id=%s"
        cursor.execute(sql, [id])
        res = cursor.fetchone()
        if res is None:
            raise NotFoundException
        self.id = res[0]
        self.text = res[1]
        self.answers = DBAnswer.loadByQuestionId(self.id)

    @staticmethod
    def getAll():
        db = database.getDbConnection()
        cursor = db.cursor()
        sql = "SELECT * FROM question"
        cursor.execute(sql)
        res = cursor.fetchall()
        questions = []
        for id,text in res:
            q = DBQuestion()
            q.id = id
            q.text = text
            q.answers = DBAnswer.loadByQuestionId(q.id)
            questions.append(q)
        return questions

    def jsonify(self):
        return {"question_id": self.id,
                "text": self.text,
                "answers": [a.jsonify() for a in self.answers]}
